import unittest
import port_scanner

class UnitTests(unittest.TestCase):
    def test_port_scanner_ip(self):
        ports = port_scanner.get_open_ports('209.216.230.240', [440, 445], False)
        actual = ports
        expected = [443]
        self.assertEqual(actual, expected, 'Expected scanning IP to return [443]')

    def test_port_scanner_url(self):
        ports = port_scanner.get_open_ports('www.stackoverflow.com', [79, 82], False)
        actual = ports
        expected = [80]
        self.assertEqual(actual, expected, 'Expected scanning URL to return [80]')

    def test_port_scanner_url_multiple_ports(self):
        ports = port_scanner.get_open_ports('scanme.nmap.org', [20, 80], False)
        actual = ports
        expected = [22, 80]
        self.assertEqual(actual, expected, 'Expected scanning URL to return [22, 80]')

    def test_port_scanner_verbose_ip(self):
        str = port_scanner.get_open_ports('104.26.10.233', [440, 450], True)
        actual = str
        # Note: The expected string might vary slightly depending on DNS resolution names
        # We check key parts of the string
        self.assertTrue("Open ports for" in actual, 'Expected "Open ports for" in verbose output')
        self.assertTrue("104.26.10.233" in actual, 'Expected IP address in verbose output')
        self.assertTrue("443" in actual, 'Expected port 443 in verbose output')
        self.assertTrue("https" in actual, 'Expected service name "https" in verbose output')

    def test_port_scanner_verbose_url(self):
        str = port_scanner.get_open_ports('scanme.nmap.org', [20, 80], True)
        actual = str
        self.assertTrue("Open ports for scanme.nmap.org" in actual, 'Expected verbose header')
        self.assertTrue("22" in actual and "ssh" in actual, 'Expected ssh entry')
        self.assertTrue("80" in actual and "http" in actual, 'Expected http entry')

    def test_port_scanner_invalid_hostname(self):
        err = port_scanner.get_open_ports('scanme.nmap', [22, 42], False)
        actual = err
        expected = "Error: Invalid hostname"
        self.assertEqual(actual, expected, 'Expected "Error: Invalid hostname"')

    def test_port_scanner_invalid_ip_address(self):
        err = port_scanner.get_open_ports('266.255.9.9', [22, 42], False)
        actual = err
        expected = "Error: Invalid IP address"
        self.assertEqual(actual, expected, 'Expected "Error: Invalid IP address"')

if __name__ == "__main__":
    unittest.main()