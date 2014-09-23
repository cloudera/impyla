#include "impala-precompiled.h"
#include <cstring>
#include <cctype>
#include <limits>

#define IS_SPACE(c) ((c) == ' ' || (c) == '\t' || (c) == '\n' || (c) == '\v' || (c) == '\f' || (c) == '\r')

bool EqStringValImpl(const StringVal& s1, const StringVal& s2) {
    if (s1.is_null != s2.is_null)
        return false;
    if (s1.is_null)
        return true;
    if (s1.len != s2.len)
        return false;
    return (s1.ptr == s2.ptr) || memcmp(s1.ptr, s2.ptr, s1.len) == 0;
}

// TODO(laserson): figure out what to do with NULLs (error?)
StringVal GetItemStringValImpl(const StringVal& s, int i) {
    if (s.is_null) return StringVal::null();
    if ((i < -s.len) || (i >= s.len)) return StringVal::null();
    int offset = (i >= 0) ? i : (s.len + i);
    StringVal retval(s.ptr + offset, 1);
    return retval;
}

StringVal AddStringValImpl(FunctionContext* context, const StringVal& s1, const StringVal& s2) {
    if (s1.is_null || s2.is_null) {
        context->AddWarning("AddStringValImpl: attempted to concat NULL string; returning NULL");
        return StringVal::null();
    }
    if (s1.len == 0) return s2;
    if (s2.len == 0) return s1;
    StringVal retval(context, s1.len + s2.len);
    memcpy(retval.ptr, s1.ptr, s1.len);
    memcpy(retval.ptr + s1.len, s2.ptr, s2.len);
    return retval;
}


// Python string module

StringVal StringCapitalizeImpl(FunctionContext* context, const StringVal& s) {
    if (s.is_null) return StringVal::null();
    if (s.len == 0) return s;
    StringVal upper(context, s.len);
    for (int i = 0; i < s.len; i++) {
        upper.ptr[i] = toupper(s.ptr[i]);
    }
    return upper;
}

int StringSplitWhitespace(const StringVal& s, StringVal* arr, int maxcount) {
    // assumes s.len > 0 and splitting on whitespace
    int i = 0, j = 0, count = 0;
    while (maxcount-- > 0) {
        // skip leading whitespace
        while (i < s.len && IS_SPACE(s.ptr[i]))
            i++;
        if (i == s.len) break;
        j = i; i++;
        while (i < s.len && !IS_SPACE(s.ptr[i]))
            i++;
        if (arr)
            arr[count] = StringVal(s.ptr + j, i - j);
        count++;
    }
    if (i < s.len) {
        // maxcount has been reached; skip any remaining whitespace and add another token
        while (i < s.len && IS_SPACE(s.ptr[i]))
            i++;
        if (i != s.len)
            if (arr)
                arr[count] = StringVal(s.ptr + i, s.len - i);
            count++;
    }
    return count;
}

int StringSplitChar(const StringVal& s, StringVal* arr, uint8_t sep, int maxcount) {
    // assumes s.len > 0 and splitting on a single char
    int i = 0, j = 0, count = 0;
    while ((j < s.len) && (maxcount-- > 0)) {
        for (; j < s.len; j++) {
            if (s.ptr[j] == sep) {
                if (arr)
                    arr[count] = StringVal(s.ptr + i, j - i);
                count++;
                j++; i = j;
                break;
            }
        }
    }
    if (i <= s.len) {
        if (arr)
            arr[count] = StringVal(s.ptr + i, s.len - i);
        count++;
    }
    return count;
}

int naive_memmem(const uint8_t* s, int s_len, const uint8_t* sep, int sep_len) {
    int i = 0;
    while (i + sep_len <= s_len) {
        if (memcmp(s + i, sep, sep_len) == 0)
            return i;
    }
    return -1;
}

int StringSplitSep(const StringVal& s, StringVal* arr, const StringVal& sep, int maxcount) {
    int i = 0, pos = 0, count = 0;
    while (maxcount-- > 0) {
        pos = naive_memmem(s.ptr + i, s.len - i, sep.ptr, sep.len);
        if (pos < 0)
            break;
        if (arr)
            arr[count] = StringVal(s.ptr + i, pos);
        count++;
        i += pos + sep.len;
    }
    if (arr)
        arr[count] = StringVal(s.ptr + i, s.len - i);
    count++;
    return count;
}

// NOTE: the returned StringVal buffer contains an array of StringVal objects
StringVal StringSplitImpl(FunctionContext* context, const StringVal& s, const StringVal& sep, const IntVal& maxsplit) {
    // Check for 'error' cases
    if (s.is_null) {
        context->AddWarning("StringSplitImpl: string to split is null");
        return StringVal::null();
    }
    if (!sep.is_null && sep.len == 0) {
        context->AddWarning("StringSplitImpl: separator is empty string");
        return StringVal::null();
    }
    if (s.len == 0 && sep.is_null) {
        // return empty list
        StringVal arr(context, 0);
        return arr;
    }
    if (s.len == 0 && sep.len > 0) {
        StringVal arr(context, sizeof(StringVal));
        reinterpret_cast<StringVal*>(arr.ptr)[0] = StringVal("");
        return arr;
    }
    // s.len > 0
    // following impl is from CPython
    int maxcount = (maxsplit.is_null || maxsplit.val < 0) ? std::numeric_limits<int>::max() : maxsplit.val;
    if (sep.is_null) {
        // split on whitespace
        int count = StringSplitWhitespace(s, NULL, maxcount);
        StringVal arr(context, sizeof(StringVal) * count);
        StringSplitWhitespace(s, reinterpret_cast<StringVal*>(arr.ptr), maxcount);
        return arr;
    }
    if (sep.len == 1) {
        // split on char
        int count = StringSplitChar(s, NULL, sep.ptr[0], maxcount);
        StringVal arr(context, sizeof(StringVal) * count);
        StringSplitChar(s, reinterpret_cast<StringVal*>(arr.ptr), sep.ptr[0], maxcount);
        return arr;
    }
    // else sep.len > 1
    // split on sep
    int count = StringSplitSep(s, NULL, sep, maxcount);
    StringVal arr(context, sizeof(StringVal) * count);
    StringSplitSep(s, reinterpret_cast<StringVal*>(arr.ptr), sep, maxcount);
    return arr;
}
