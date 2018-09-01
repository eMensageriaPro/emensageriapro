# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5001', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5001calcterc',
            name='tpcr',
            field=models.IntegerField(choices=[(108201, '108201 - Contribui\xe7\xe3o previdenci\xe1ria (CP) descontada do segurado empregado/avulso, al\xedquotas 8%, 9% ou 11%'), (108202, '108202 - CP descontada do segurado empregado rural curto prazo, al\xedquota de 8%, lei 11718/2008'), (108203, '108203 - CP descontada do segurado empregado dom\xe9stico ou segurado especial, al\xedquota de 8%, 9% ou 11%'), (108204, '108204 - CP descontada do segurado especial curto prazo, al\xedquota de 8%, lei 11718/2008'), (108221, '108221 - CP descontada do segurado empregado/avulso 13\xb0 sal\xe1rio, al\xedquotas 8%, 9% ou 11% (codIncCP = [12, 16])'), (108222, '108222 - CP descontada do segurado empregado rural curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (108223, '108223 - CP descontada do segurado empregado dom\xe9stico ou segurado especial 13\xb0 sal\xe1rio, al\xedquota de 8%, 9% ou 11%(codIncCP = [12, 16])'), (108224, '108224 - CP descontada do segurado especial curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (109901, '109901 - CP descontada do contribuinte individual, al\xedquota de 11%'), (109902, '109902 - CP descontada do contribuinte individual, al\xedquota de 20%'), (b'1218-02', '1218-02 - Contribui\xe7\xe3o ao SEST, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,5%'), (b'1221-02', '1221-02 - Contribui\xe7\xe3o ao SENAT, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,0%')]),
        ),
        migrations.AlterField(
            model_name='s5001infocpcalc',
            name='tpcr',
            field=models.IntegerField(choices=[(108201, '108201 - Contribui\xe7\xe3o previdenci\xe1ria (CP) descontada do segurado empregado/avulso, al\xedquotas 8%, 9% ou 11%'), (108202, '108202 - CP descontada do segurado empregado rural curto prazo, al\xedquota de 8%, lei 11718/2008'), (108203, '108203 - CP descontada do segurado empregado dom\xe9stico ou segurado especial, al\xedquota de 8%, 9% ou 11%'), (108204, '108204 - CP descontada do segurado especial curto prazo, al\xedquota de 8%, lei 11718/2008'), (108221, '108221 - CP descontada do segurado empregado/avulso 13\xb0 sal\xe1rio, al\xedquotas 8%, 9% ou 11% (codIncCP = [12, 16])'), (108222, '108222 - CP descontada do segurado empregado rural curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (108223, '108223 - CP descontada do segurado empregado dom\xe9stico ou segurado especial 13\xb0 sal\xe1rio, al\xedquota de 8%, 9% ou 11%(codIncCP = [12, 16])'), (108224, '108224 - CP descontada do segurado especial curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (109901, '109901 - CP descontada do contribuinte individual, al\xedquota de 11%'), (109902, '109902 - CP descontada do contribuinte individual, al\xedquota de 20%'), (b'1218-02', '1218-02 - Contribui\xe7\xe3o ao SEST, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,5%'), (b'1221-02', '1221-02 - Contribui\xe7\xe3o ao SENAT, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,0%')]),
        ),
    ]
