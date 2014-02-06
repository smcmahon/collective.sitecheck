import argparse
import gzip
import StringIO
import urllib2
import xml.etree.ElementTree as ElementTree


def sitecheck():
    parser = argparse.ArgumentParser(description='Check a site via sitemap.')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('sitemap_url', help='URL of sitemap.xml.gz')
    args = parser.parse_args()
    verbose = args.verbose
    if verbose:
        print "Opening:", args.sitemap_url
    sitemap_f = urllib2.urlopen(args.sitemap_url)
    f = StringIO.StringIO(sitemap_f.read())
    gz_f = gzip.GzipFile(fileobj=f)
    s = gz_f.read()
    root = ElementTree.fromstring(s)
    for child in root.iter():
        if '}loc' in child.tag:
            url = child.text.strip()
            try:
                f = urllib2.urlopen(url)
                if verbose:
                    print "success", url
                continue
            except urllib2.HTTPError, e:
                print e.code, url
                if e.code != 404:
                    break
            except urllib2.URLError, e:
                print e.reason.errno, url
            # break
    pass
