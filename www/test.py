#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Pengfei, Li'

import www.orm
from www.models import User
import asyncio
import random


async def test(loop):
    await www.orm.create_pool(loop, user='root', password='root', db='awesome')
    u = User(name='Test', email='test%s@example.com' % random.randint(0, 10000000), passwd='123', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
