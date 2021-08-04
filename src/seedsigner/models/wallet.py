
class Wallet:

    QRLOW = 0
    QRMEDIUM = 1
    QRHIGH = 2

    def __init__(self, wallet_name, network="main", qr_density=1, policy="PKWSH"):
        self.network = network
        self.qr_density = qr_density
        self.policy = policy
        self.wallet_name = wallet_name

    @property
    def wallet_name(self):
        return self._wallet_name

    @wallet_name.setter
    def wallet_name(self, value):
        if value in ("Specter Desktop", "Blue Wallet", "Sparrow", "UR 2.0 Generic"):
            self._wallet_name = value
        else:
            raise Exception("Unexpected Wallet wallet_name value")

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, value):
        self._network = value

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        if value in ("PKWSH", "PKWPKH"):
            self._policy = value
        else:
            raise Exception("Unexpected Wallet policy value")

    @property
    def policy_name(self):
        if self.policy == "PKWSH":
            return "Multi Sig"
        elif self.policy == "PKWPKH":
            return "Single Sig"
        else:
            raise Exception("Unexpected Wallet policy value")

    @property
    def qr_density(self):
        return self._qr_density

    @qr_density.setter
    def qr_density(self, value):
        if value in (Wallet.QRLOW, Wallet.QRMEDIUM, Wallet.QRHIGH):
            self._qr_density = value
        else:
            raise Exception("Invalid Wallet QR density value")

    @property
    def qr_density_name(self):
        if self.qr_density == Wallet.QRLOW:
            return "Low"
        elif self.qr_density == Wallet.QRMEDIUM:
            return "Medium"
        elif self.qr_density == Wallet.QRHIGH:
            return "High"
        else:
            return "Unknown"

    @property
    def derivation(self):
        if self.policy == "PKWSH" and self.network == "main":
            return "m/48h/0h/0h/2h"
        elif self.policy == "PKWSH" and self.network == "test":
            return "m/48h/1h/0h/2h"
        elif self.policy == "PKWPKH" and self.network == "main":
            return "m/84h/0h/0h"
        elif self.policy == "PKWPKH" and self.network == "test":
            return "m/84h/1h/0h"
        else:
            raise Exception("Unsupported Derivation Path or Policy")