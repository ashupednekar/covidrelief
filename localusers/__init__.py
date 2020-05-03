# from localusers.models import Limits
#
# def save_to_db(country, transaction_type, min, max):
#     min = int(min)
#     if max == 'no limit':
#         max = None
#     else:
#         max = int(max.replace(',', ''))
#     l = Limits(country=country, transaction_type=transaction_type, min_amount=min, max_amount=max)
#     l.save()
#
# factory_shipped_data = [   # country,  transaction_type, min_amount, max_amount
#     ['Kenya',  'Own accounts',                                                          '1',       '5,000,000'],
#     ['Kenya',  'Within I&M Bank accounts',                                              '1',       '5,000,000'],
#     #
#     ['Rwanda', 'Internal transfers- Own Account',                                       '1',       'no limit'],
#     ['Rwanda', 'Internal transfers- Other Account - With half-kyc (Bene & Ad-hoc)',     '1',       '250,000'],
#     ['Rwanda', 'Internal transfers- Other Account – Ad-hoc',                            '1',       '250,000'],
#     ['Rwanda', 'Internal transfers- Other Account - Beneficiary Based',                 '1',       '5,000,000'],
#     ['Rwanda', 'Mobile Money -  With Half-kyc (Bene & Ad-hoc)',                         '1',       '250,000'],
#     ['Rwanda', 'Mobile Money – Ad-hoc',                                                 '1',       '250,000'],
#     ['Rwanda', 'Mobile Money - Beneficiary Based',                                      '1',       '1,000,000'],
#     ['Rwanda', 'Airtime Purchase - With half-kyc (Bene & Ad-hoc)',                      '1',       '250,000'],
#     ['Rwanda', 'Airtime Purchase – Ad-hoc',                                             '1',       '250,000'],
#     ['Rwanda', 'Airtime Purchase - Beneficiary Based',                                  '1',       '1,000,000'],
#     #
#     ['Tanzania', 'Internal transfers- Own Account',                                     '1',       'no limit'],
#     ['Tanzania', 'Internal transfers- Other Account – Ad-hoc',                          '1',       '20,000,000'],
#     ['Tanzania', 'Internal transfers- Other Account - Beneficiary Based',               '1',       '20,000,000'],
#     ['Tanzania', 'Mobile Money – Ad-hoc',                                               '1',       '1,000,000'],
#     ['Tanzania', 'Mobile Money - Beneficiary Based',                                    '1',       '1,000,000'],
#     ['Tanzania', 'Airtime Purchase – Ad-hoc',                                           '1',       '1,000,000'],
#     ['Tanzania', 'Airtime Purchase - Beneficiary Based',                                '1',       '1,000,000'],
# ]
#
# for x in factory_shipped_data:
#     save_to_db(x[0], x[1], x[2], x[3])