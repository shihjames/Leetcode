class Solution:
    def defangIPaddr(self, address: str) -> str:
        add_list = address.split(".")
        return "[.]".join(add_list)