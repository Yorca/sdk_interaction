import pdfkit

url = "https://yandex.com/dev/mobile-ads/doc/android/quick-start/gdpr-about.html"
output_file = "test_optout.pdf"

pdfkit.from_url(url, output_file)