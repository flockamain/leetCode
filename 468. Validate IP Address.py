"""Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address."""
def validIPAddress(self, queryIP):
        #check if the queryIP is an IPv4 address
        if queryIP.count('.') == 3:
            octets = queryIP.split('.')
            for octet in octets:
                #check if the octet is a number between 0 and 255, and does not have leading zeros
                if not octet.isdigit() or int(octet) < 0 or int(octet) > 255 or (octet[0] == '0' and len(octet) > 1):
                    return "Neither"
            return "IPv4"
        # check if the queryIP is an IPv6 address
        elif ':' in queryIP:
            """
        # Handle :: compression
            if '::' in queryIP:
            # '::' can only appear once
                if queryIP.count('::') > 1:
                    return "Neither"
            
                # Split into left and right sides of '::'
                left, right = queryIP.split('::')
                left_hextets  = left.split(':')  if left  else []
                right_hextets = right.split(':') if right else []
            
                # Calculate how many zero hextets '::' represents
                missing = 8 - len(left_hextets) - len(right_hextets)
                if missing < 1:
                    return "Neither"
            
                hextets = left_hextets + ['0'] * missing + right_hextets
            else:
                hextets = queryIP.split(':')"""
            hextets = queryIP.split(':')

            # Must have exactly 8 hextets
            if len(hextets) != 8:
                return "Neither"

            for hextet in hextets:
                if len(hextet) == 0 or len(hextet) > 4 or not all(c in '0123456789abcdefABCDEF' for c in hextet):
                    return "Neither"
            return "IPv6"

        else:
                return "Neither"
