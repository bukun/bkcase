#!/usr/bin/python3

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

piwik_str = '''
<!-- Piwik -->
<script type="text/javascript">
var _paq = _paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var u="//121.42.45.218/piwik/";
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', '3']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
    })();
</script>
<!-- End Piwik Code -->
</html>
'''

for wroot, wdirs, wfiles in os.walk(os.getcwd()):
    for wfile in wfiles:
        if wfile.lower().endswith('.html'):
            the_file = os.path.join(wroot, wfile)
            print(the_file)
            cnts = open(the_file).read()
            sig = False
            if 'ca-pub-4505825019574578' in cnts:
                print('skip')
            else:
                cnts = cnts.replace('</head>', ad_str)
                sig = True

            if 'piwik.php' in cnts:
                print('got piwik')
            else:
                cnts = cnts.replace('</html>', piwik_str)
                sig = True
            if sig:
                with open(the_file, 'w' ) as fo:
                    fo.write(cnts)

