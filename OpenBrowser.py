import os
import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Browser")
root.geometry('410x175')
root.config(bg='#AAE7FD')
root.minsize(410, 175)
root.maxsize(410, 175)

lan = ['bn : Bengali', 'en : English', 'ru : Russian', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic',
       'ar : Arabic', 'hy : Armenian', 'as : Assamese',
       'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara', 'eu : Basque', 'be : Belarusian',
       'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian', 'ca : Catalan', 'ceb : Cebuano', 'ny : Chichewa',
       'zh-CN : Chinese (Simplified)', 'zh-TW : Chinese (Traditional)', 'co : Corsican', 'hr : Croatian', 'cs : Czech',
       'da : Danish', 'dv : Dhivehi', 'doi : Dogri', 'nl : Dutch', 'eo : Esperanto', 'et : Estonian',
       'ee : Ewe', 'tl : Filipino', 'fi : Finnish', 'fr : French', 'fy : Frisian', 'gl : Galician', 'ka : Georgian',
       'de : German', 'el : Greek', 'gn : Guarani', 'gu : Gujarati', 'ht : Haitian Creole', 'ha : Hausa',
       'haw : Hawaiian', 'iw : Hebrew', 'hi : Hindi', 'hmn : Hmong', 'hu : Hungarian', 'is : Icelandic', 'ig : Igbo',
       'ilo : Ilocano', 'id : Indonesian', 'ga : Irish', 'it : Italian', 'ja : Japanese', 'jw : Javanese',
       'kn : Kannada', 'kk : Kazakh', 'km : Khmer', 'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio',
       'ku : Kurdish (Kurmanji)', 'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian',
       'ln : Lingala', 'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili',
       'mg : Malagasy', 'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi',
       'mni-Mtei : Meiteilon (Manipuri)', 'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali',
       'no : Norwegian', 'or : Odia (Oriya)', 'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish',
       'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua', 'ro : Romanian', 'sm : Samoan',
       'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi', 'sr : Serbian', 'st : Sesotho', 'sn : Shona',
       'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian', 'so : Somali', 'es : Spanish', 'su : Sundanese',
       'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil', 'tt : Tatar', 'te : Telugu', 'th : Thai',
       'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen', 'ak : Twi', 'uk : Ukrainian', 'ur : Urdu',
       'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh', 'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba',
       'zu : Zulu', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic', 'ar : Arabic', 'hy : Armenian', 'as : Assamese',
       'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara', 'eu : Basque', 'be : Belarusian', 'bn : Bengali',
       'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian', 'ca : Catalan', 'ceb : Cebuano', 'ny : Chichewa',
       'zh-CN : Chinese (Simplified)', 'zh-TW : Chinese (Traditional)', 'co : Corsican', 'hr : Croatian', 'cs : Czech',
       'da : Danish', 'dv : Dhivehi', 'doi : Dogri', 'nl : Dutch', 'en : English', 'eo : Esperanto', 'et : Estonian',
       'ee : Ewe', 'tl : Filipino', 'fi : Finnish', 'fr : French', 'fy : Frisian', 'gl : Galician', 'ka : Georgian',
       'de : German', 'el : Greek', 'gn : Guarani', 'gu : Gujarati', 'ht : Haitian Creole', 'ha : Hausa',
       'haw : Hawaiian', 'iw : Hebrew', 'hi : Hindi', 'hmn : Hmong', 'hu : Hungarian', 'is : Icelandic', 'ig : Igbo',
       'ilo : Ilocano', 'id : Indonesian', 'ga : Irish', 'it : Italian', 'ja : Japanese', 'jw : Javanese',
       'kn : Kannada', 'kk : Kazakh', 'km : Khmer', 'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio',
       'ku : Kurdish (Kurmanji)', 'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian',
       'ln : Lingala', 'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili',
       'mg : Malagasy', 'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi',
       'mni-Mtei : Meiteilon (Manipuri)', 'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali',
       'no : Norwegian', 'or : Odia (Oriya)', 'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish',
       'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua', 'ro : Romanian', 'ru : Russian', 'sm : Samoan',
       'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi', 'sr : Serbian', 'st : Sesotho', 'sn : Shona',
       'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian', 'so : Somali', 'es : Spanish', 'su : Sundanese',
       'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil', 'tt : Tatar', 'te : Telugu', 'th : Thai',
       'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen', 'ak : Twi', 'uk : Ukrainian', 'ur : Urdu',
       'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh', 'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba',
       'zu : Zulu', 'auto : Detect language', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic', 'ar : Arabic',
       'hy : Armenian', 'as : Assamese', 'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara', 'eu : Basque',
       'be : Belarusian', 'bn : Bengali', 'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian', 'ca : Catalan',
       'ceb : Cebuano', 'ny : Chichewa', 'zh-CN : Chinese (Simplified)', 'zh-TW : Chinese (Traditional)',
       'co : Corsican', 'hr : Croatian', 'cs : Czech', 'da : Danish', 'dv : Dhivehi', 'doi : Dogri', 'nl : Dutch',
       'en : English', 'eo : Esperanto', 'et : Estonian', 'ee : Ewe', 'tl : Filipino', 'fi : Finnish', 'fr : French',
       'fy : Frisian', 'gl : Galician', 'ka : Georgian', 'de : German', 'el : Greek', 'gn : Guarani', 'gu : Gujarati',
       'ht : Haitian Creole', 'ha : Hausa', 'haw : Hawaiian', 'iw : Hebrew', 'hi : Hindi', 'hmn : Hmong',
       'hu : Hungarian', 'is : Icelandic', 'ig : Igbo', 'ilo : Ilocano', 'id : Indonesian', 'ga : Irish',
       'it : Italian', 'ja : Japanese', 'jw : Javanese', 'kn : Kannada', 'kk : Kazakh', 'km : Khmer',
       'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio', 'ku : Kurdish (Kurmanji)',
       'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian', 'ln : Lingala',
       'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili', 'mg : Malagasy',
       'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi', 'mni-Mtei : Meiteilon (Manipuri)',
       'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali', 'no : Norwegian', 'or : Odia (Oriya)',
       'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish', 'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua',
       'ro : Romanian', 'ru : Russian', 'sm : Samoan', 'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi',
       'sr : Serbian', 'st : Sesotho', 'sn : Shona', 'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian',
       'so : Somali', 'es : Spanish', 'su : Sundanese', 'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil',
       'tt : Tatar', 'te : Telugu', 'th : Thai', 'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen',
       'ak : Twi', 'uk : Ukrainian', 'ur : Urdu', 'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh',
       'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba', 'zu : Zulu', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic',
       'ar : Arabic', 'hy : Armenian', 'as : Assamese', 'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara',
       'eu : Basque', 'be : Belarusian', 'bn : Bengali', 'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian',
       'ca : Catalan', 'ceb : Cebuano', 'ny : Chichewa', 'zh-CN : Chinese (Simplified)',
       'zh-TW : Chinese (Traditional)', 'co : Corsican', 'hr : Croatian', 'cs : Czech', 'da : Danish', 'dv : Dhivehi',
       'doi : Dogri', 'nl : Dutch', 'en : English', 'eo : Esperanto', 'et : Estonian', 'ee : Ewe', 'tl : Filipino',
       'fi : Finnish', 'fr : French', 'fy : Frisian', 'gl : Galician', 'ka : Georgian', 'de : German', 'el : Greek',
       'gn : Guarani', 'gu : Gujarati', 'ht : Haitian Creole', 'ha : Hausa', 'haw : Hawaiian', 'iw : Hebrew',
       'hi : Hindi', 'hmn : Hmong', 'hu : Hungarian', 'is : Icelandic', 'ig : Igbo', 'ilo : Ilocano', 'id : Indonesian',
       'ga : Irish', 'it : Italian', 'ja : Japanese', 'jw : Javanese', 'kn : Kannada', 'kk : Kazakh', 'km : Khmer',
       'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio', 'ku : Kurdish (Kurmanji)',
       'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian', 'ln : Lingala',
       'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili', 'mg : Malagasy',
       'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi', 'mni-Mtei : Meiteilon (Manipuri)',
       'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali', 'no : Norwegian', 'or : Odia (Oriya)',
       'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish', 'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua',
       'ro : Romanian', 'ru : Russian', 'sm : Samoan', 'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi',
       'sr : Serbian', 'st : Sesotho', 'sn : Shona', 'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian',
       'so : Somali', 'es : Spanish', 'su : Sundanese', 'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil',
       'tt : Tatar', 'te : Telugu', 'th : Thai', 'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen',
       'ak : Twi', 'uk : Ukrainian', 'ur : Urdu', 'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh',
       'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba', 'zu : Zulu', 'auto : Detect language', 'af : Afrikaans',
       'sq : Albanian', 'am : Amharic', 'ar : Arabic', 'hy : Armenian', 'as : Assamese', 'ay : Aymara',
       'az : Azerbaijani', 'bm : Bambara', 'eu : Basque', 'be : Belarusian', 'bn : Bengali', 'bho : Bhojpuri',
       'bs : Bosnian', 'bg : Bulgarian', 'ca : Catalan', 'ceb : Cebuano', 'ny : Chichewa',
       'zh-CN : Chinese (Simplified)', 'zh-TW : Chinese (Traditional)', 'co : Corsican', 'hr : Croatian', 'cs : Czech',
       'da : Danish', 'dv : Dhivehi', 'doi : Dogri', 'nl : Dutch', 'en : English', 'eo : Esperanto', 'et : Estonian',
       'ee : Ewe', 'tl : Filipino', 'fi : Finnish', 'fr : French', 'fy : Frisian', 'gl : Galician', 'ka : Georgian',
       'de : German', 'el : Greek', 'gn : Guarani', 'gu : Gujarati', 'ht : Haitian Creole', 'ha : Hausa',
       'haw : Hawaiian', 'iw : Hebrew', 'hi : Hindi', 'hmn : Hmong', 'hu : Hungarian', 'is : Icelandic', 'ig : Igbo',
       'ilo : Ilocano', 'id : Indonesian', 'ga : Irish', 'it : Italian', 'ja : Japanese', 'jw : Javanese',
       'kn : Kannada', 'kk : Kazakh', 'km : Khmer', 'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio',
       'ku : Kurdish (Kurmanji)', 'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian',
       'ln : Lingala', 'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili',
       'mg : Malagasy', 'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi',
       'mni-Mtei : Meiteilon (Manipuri)', 'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali',
       'no : Norwegian', 'or : Odia (Oriya)', 'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish',
       'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua', 'ro : Romanian', 'ru : Russian', 'sm : Samoan',
       'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi', 'sr : Serbian', 'st : Sesotho', 'sn : Shona',
       'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian', 'so : Somali', 'es : Spanish', 'su : Sundanese',
       'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil', 'tt : Tatar', 'te : Telugu', 'th : Thai',
       'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen', 'ak : Twi', 'uk : Ukrainian', 'ur : Urdu',
       'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh', 'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba',
       'zu : Zulu', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic', 'ar : Arabic', 'hy : Armenian', 'as : Assamese',
       'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara', 'eu : Basque', 'be : Belarusian', 'bn : Bengali',
       'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian', 'ca : Catalan', 'ceb : Cebuano', 'ny : Chichewa',
       'zh-CN : Chinese (Simplified)', 'zh-TW : Chinese (Traditional)', 'co : Corsican', 'hr : Croatian', 'cs : Czech',
       'da : Danish', 'dv : Dhivehi', 'doi : Dogri', 'nl : Dutch', 'en : English', 'eo : Esperanto', 'et : Estonian',
       'ee : Ewe', 'tl : Filipino', 'fi : Finnish', 'fr : French', 'fy : Frisian', 'gl : Galician', 'ka : Georgian',
       'de : German', 'el : Greek', 'gn : Guarani', 'gu : Gujarati', 'ht : Haitian Creole', 'ha : Hausa',
       'haw : Hawaiian', 'iw : Hebrew', 'hi : Hindi', 'hmn : Hmong', 'hu : Hungarian', 'is : Icelandic', 'ig : Igbo',
       'ilo : Ilocano', 'id : Indonesian', 'ga : Irish', 'it : Italian', 'ja : Japanese', 'jw : Javanese',
       'kn : Kannada', 'kk : Kazakh', 'km : Khmer', 'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio',
       'ku : Kurdish (Kurmanji)', 'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian',
       'ln : Lingala', 'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili',
       'mg : Malagasy', 'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi',
       'mni-Mtei : Meiteilon (Manipuri)', 'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali',
       'no : Norwegian', 'or : Odia (Oriya)', 'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish',
       'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua', 'ro : Romanian', 'ru : Russian', 'sm : Samoan',
       'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi', 'sr : Serbian', 'st : Sesotho', 'sn : Shona',
       'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian', 'so : Somali', 'es : Spanish', 'su : Sundanese',
       'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil', 'tt : Tatar', 'te : Telugu', 'th : Thai',
       'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen', 'ak : Twi', 'uk : Ukrainian', 'ur : Urdu',
       'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh', 'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba',
       'zu : Zulu', 'auto : Detect language', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic', 'ar : Arabic',
       'hy : Armenian', 'as : Assamese', 'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara', 'eu : Basque',
       'be : Belarusian', 'bn : Bengali', 'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian', 'ca : Catalan',
       'ceb : Cebuano', 'ny : Chichewa', 'zh-CN : Chinese (Simplified)', 'zh-TW : Chinese (Traditional)',
       'co : Corsican', 'hr : Croatian', 'cs : Czech', 'da : Danish', 'dv : Dhivehi', 'doi : Dogri', 'nl : Dutch',
       'en : English', 'eo : Esperanto', 'et : Estonian', 'ee : Ewe', 'tl : Filipino', 'fi : Finnish', 'fr : French',
       'fy : Frisian', 'gl : Galician', 'ka : Georgian', 'de : German', 'el : Greek', 'gn : Guarani', 'gu : Gujarati',
       'ht : Haitian Creole', 'ha : Hausa', 'haw : Hawaiian', 'iw : Hebrew', 'hi : Hindi', 'hmn : Hmong',
       'hu : Hungarian', 'is : Icelandic', 'ig : Igbo', 'ilo : Ilocano', 'id : Indonesian', 'ga : Irish',
       'it : Italian', 'ja : Japanese', 'jw : Javanese', 'kn : Kannada', 'kk : Kazakh', 'km : Khmer',
       'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio', 'ku : Kurdish (Kurmanji)',
       'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian', 'ln : Lingala',
       'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili', 'mg : Malagasy',
       'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi', 'mni-Mtei : Meiteilon (Manipuri)',
       'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali', 'no : Norwegian', 'or : Odia (Oriya)',
       'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish', 'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua',
       'ro : Romanian', 'ru : Russian', 'sm : Samoan', 'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi',
       'sr : Serbian', 'st : Sesotho', 'sn : Shona', 'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian',
       'so : Somali', 'es : Spanish', 'su : Sundanese', 'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil',
       'tt : Tatar', 'te : Telugu', 'th : Thai', 'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen',
       'ak : Twi', 'uk : Ukrainian', 'ur : Urdu', 'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh',
       'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba', 'zu : Zulu', 'af : Afrikaans', 'sq : Albanian', 'am : Amharic',
       'ar : Arabic', 'hy : Armenian', 'as : Assamese', 'ay : Aymara', 'az : Azerbaijani', 'bm : Bambara',
       'eu : Basque', 'be : Belarusian', 'bn : Bengali', 'bho : Bhojpuri', 'bs : Bosnian', 'bg : Bulgarian',
       'ca : Catalan', 'ceb : Cebuano', 'ny : Chichewa', 'zh-CN : Chinese (Simplified)',
       'zh-TW : Chinese (Traditional)', 'co : Corsican', 'hr : Croatian', 'cs : Czech', 'da : Danish', 'dv : Dhivehi',
       'doi : Dogri', 'nl : Dutch', 'en : English', 'eo : Esperanto', 'et : Estonian', 'ee : Ewe', 'tl : Filipino',
       'fi : Finnish', 'fr : French', 'fy : Frisian', 'gl : Galician', 'ka : Georgian', 'de : German', 'el : Greek',
       'gn : Guarani', 'gu : Gujarati', 'ht : Haitian Creole', 'ha : Hausa', 'haw : Hawaiian', 'iw : Hebrew',
       'hi : Hindi', 'hmn : Hmong', 'hu : Hungarian', 'is : Icelandic', 'ig : Igbo', 'ilo : Ilocano', 'id : Indonesian',
       'ga : Irish', 'it : Italian', 'ja : Japanese', 'jw : Javanese', 'kn : Kannada', 'kk : Kazakh', 'km : Khmer',
       'rw : Kinyarwanda', 'gom : Konkani', 'ko : Korean', 'kri : Krio', 'ku : Kurdish (Kurmanji)',
       'ckb : Kurdish (Sorani)', 'ky : Kyrgyz', 'lo : Lao', 'la : Latin', 'lv : Latvian', 'ln : Lingala',
       'lt : Lithuanian', 'lg : Luganda', 'lb : Luxembourgish', 'mk : Macedonian', 'mai : Maithili', 'mg : Malagasy',
       'ms : Malay', 'ml : Malayalam', 'mt : Maltese', 'mi : Maori', 'mr : Marathi', 'mni-Mtei : Meiteilon (Manipuri)',
       'lus : Mizo', 'mn : Mongolian', 'my : Myanmar (Burmese)', 'ne : Nepali', 'no : Norwegian', 'or : Odia (Oriya)',
       'om : Oromo', 'ps : Pashto', 'fa : Persian', 'pl : Polish', 'pt : Portuguese', 'pa : Punjabi', 'qu : Quechua',
       'ro : Romanian', 'ru : Russian', 'sm : Samoan', 'sa : Sanskrit', 'gd : Scots Gaelic', 'nso : Sepedi',
       'sr : Serbian', 'st : Sesotho', 'sn : Shona', 'sd : Sindhi', 'si : Sinhala', 'sk : Slovak', 'sl : Slovenian',
       'so : Somali', 'es : Spanish', 'su : Sundanese', 'sw : Swahili', 'sv : Swedish', 'tg : Tajik', 'ta : Tamil',
       'tt : Tatar', 'te : Telugu', 'th : Thai', 'ti : Tigrinya', 'ts : Tsonga', 'tr : Turkish', 'tk : Turkmen',
       'ak : Twi', 'uk : Ukrainian', 'ur : Urdu', 'ug : Uyghur', 'uz : Uzbek', 'vi : Vietnamese', 'cy : Welsh',
       'xh : Xhosa', 'yi : Yiddish', 'yo : Yoruba', 'zu : Zulu']


def main():
    def fb():
        webbrowser.open_new('www.facebook.com')

    def yt():
        webbrowser.open_new('www.youtube.com')

    def google():
        webbrowser.open_new('www.google.com')

    def chrome():
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

    def edge():
        os.startfile(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

    def src():
        word = x.get()
        print(word)
        search = 'https://www.google.com/search?q=' + word
        print(f'searched: {search}')
        webbrowser.open_new(search)

    def trans(language='bn:Bengali'):
        language = selected_option.get().split(':')[0]
        word = x.get().split()
        text = '%20'.join(word)
        text = text.replace('?', "%3F")
        url = f"https://translate.google.com/?hl=en&tab=TT&sl=en&tl={language}&text={text}&op=translate"
        webbrowser.open_new(url)

    def default(e):
        entry.delete(0, "end")

    def OnTopScreen():
        current_state = onTop.get()
        root.attributes('-topmost', current_state)

    onTop = tk.BooleanVar()
    onTop.set(False)

    selected_option = tk.StringVar()
    selected_option.set('bn')

    x = tk.StringVar()
    b1 = tk.Button(root, text="Facebook", fg="White", bg="#3b5998",font=('Comic Sans MS', 13), command=fb)
    b2 = tk.Button(root, text="Youtube", font=('Comic Sans MS', 13), fg="White", bg="#FF0000", command=yt)
    b3 = tk.Button(root, text="Chrome", font=('Comic Sans MS', 13), fg="Black", bg="#C13584", command=chrome)
    b4 = tk.Button(root, text="MS Edge", font=('Comic Sans MS', 13), fg="Black", bg="#2bc3d2", command=edge)
    dropMenu = tk.OptionMenu(root, selected_option, *lan)
    b5 = tk.Button(root, text="Translater", fg="Black", bg="#40bfff", command=trans, padx=10, pady=2)
    b6 = tk.Button(root, text="Search", font=('Open Sans', 11),fg="White", bg="#104e92", command=src,
                   borderwidth=2, border=2)
    check_button = tk.Checkbutton(root, text="Top", variable=onTop,relief='ridge', command=OnTopScreen, bg="#AAE7FD")

    b1.place(x=10, y=100, height=30, width=190)
    b2.place(x=210, y=100, height=30, width=190)

    b3.place(x=210, y=135, height=30, width=190)
    b4.place(x=10, y=135, height=30, width=190)

    dropMenu.place(x=310, y=38, height=25, width=25)
    b5.place(x=339, y=38, height=25, width=61)
    b6.place(x=310, y=65, height=25, width=90, )

    check_button.place(x=352, y=8, )

    title = tk.Label(root, text='Personal Browser', font=('Comic Sans MS', 15), bg='#AAE7FD')
    title.place(relx=0.4, rely=0.1, anchor='center')

    entry = (tk.Entry(root, textvariable=x, border='1', borderwidth=2))
    entry.insert(0, "             Type For Search / Translate - Language ", )
    entry.place(x=10, y=40, width=290, height=50)
    entry.bind("<FocusIn>", default)
    root.mainloop()


if __name__ == '__main__':
    main()
