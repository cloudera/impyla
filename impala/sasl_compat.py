try:
    import sasl

    def build_sasl_factory(host, use_ldap, username, password, service):
        def sasl_factory():
            sasl_client = sasl.Client()
            sasl_client.setAttr("host", host)
            if use_ldap:
                sasl_client.setAttr("username", username)
                sasl_client.setAttr("password", password)
            else:
                sasl_client.setAttr("service", service)
            sasl_client.init()
            return sasl_client
        return sasl_factory

except ImportError:
    import sys
    sys.stderr.write("Unable to import 'sasl'. Fallback to 'puresasl'.")

    from puresasl.client import SASLClient, SASLError
    from contextlib import contextmanager

    @contextmanager
    def error_catcher(self, Exc = Exception):
        try:
            self.error = None
            yield
        except Exc as e:
            self.error = e.message

            
    class WrappedSASLClient(SASLClient):
        def __init__(self, *args, **kwargs):
            self.error = None
            super(WrappedSASLClient, self).__init__(*args, **kwargs)

        def start(self, mechanism):
            with error_catcher(self, SASLError):
                if isinstance(mechanism, list):
                    self.choose_mechanism(mechanism)
                else:
                    self.choose_mechanism([mechanism])
                return True, self.mechanism, self.process()
            # else
            return False, mechanism, None

        def encode(self, incoming):
            with error_catcher(self):
                return True, self.unwrap(incoming)
            # else
            return False, None
            
        def decode(self, outgoing):
            with error_catcher(self):
                return True, self.wrap(outgoing)
            # else
            return False, None
            
        def step(self, challenge):
            with error_catcher(self):
                return True, self.process(challenge)
            # else
            return False, None

        def getError(self):
            return self.error

    def build_sasl_factory(host, use_ldap, username, password, service):
        def sasl_factory():
            return WrappedSASLClient(host, username=username, password=password, service=service)
        return sasl_factory
