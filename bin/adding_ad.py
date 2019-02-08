# -*- coding:utf-8 -*-

import os
import sys
ad_str = '''<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
(adsbygoogle = window.adsbygoogle || []).push({
google_ad_client: "ca-pub-4505825019574578",
enable_page_level_ads: true
});
</script>
</head>'''

for wroot, wdirs, wfiles in os.walk(os.getcwd()):
    for wfile in wfiles:
        if wfile.lower().endswith('.html'):
            the_file = os.path.join(wroot, wfile)
            print(the_file)
            cnts = open(the_file).read()
            cnts = cnts.replace('</head>', ad_str)
            with open(the_file, 'w' ) as fo:
                fo.write(cnts)

