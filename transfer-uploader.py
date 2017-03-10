#!/usr/bin/env python2
import owncloud
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', help='Server instance', default='transfer.digilab.nfa.cz')
parser.add_argument('-u', '--user', help='Username', required=True)
parser.add_argument('-p', '--password', help='Password', required=True)
parser.add_argument('-f', '--file', help='File to share', required=True)
args = parser.parse_args()

oc = owncloud.Client('https://{0}'.format(args.server))
oc.login(args.user, args.password)
link_info = oc.share_file_with_link('/Volumes/digilab/JENKINS/{0}'.format(args.file))
oc.logout()

print '{0} : {1}'.format(args.file, link_info.get_link())
