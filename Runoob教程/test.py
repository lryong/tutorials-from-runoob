#!/usr/bin/env python
# -*- coding:utf-8 -*-

from weasyprint import HTML

HTML('AJAX.html').write_pdf('ajax.pdf')
