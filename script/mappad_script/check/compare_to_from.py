
import os

inws = r'e:\maplet_dvk\MapPicDir'

in_sig_arr  = []

publish_ws = r'e:\opt\mapws\maplet\00_China_png'



def get_published_sigs(publish_ws):
    out_arr = []
    for wroot, wdirs, wfiles in os.walk(publish_ws):
        for wfile in wfiles:
            if wfile.endswith('.png'):
                out_arr.append(wfile[:4])
    return out_arr

published_sig_arr = get_published_sigs(publish_ws)

for wroot, wdirs, wfiles in os.walk(inws):
    for wfile in wfiles:
        (qian, hou) = os.path.splitext(wfile)
        if hou.lower() in ['.jpg', '.bmp', '.tif', '.png']:
            # print(qian)
            sig_arr = qian.split('_')
            if len(sig_arr) > 1:

                sig = sig_arr[-1]
                if len(sig) == 5 and sig[0] == 's':
                    in_sig_arr.append(sig[1:])

aa = set(in_sig_arr)
bb = set(published_sig_arr)

print(aa-bb)

print(bb-aa)