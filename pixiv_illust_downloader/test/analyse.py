from bs4 import BeautifulSoup

txt="""<script>
    'use strict';
    var globalInitData = (function freeze (arg) {
            if (!Object.freeze || (arg === null || typeof arg !== 'object')) { return arg }
            for (var k in arg) {
                if (Object.prototype.hasOwnProperty.call(arg, k)) {
                    arg[k] = freeze(arg[k])
                }
            }
            return Object.freeze(arg)
        })
        


        ({
            token: "f29e4be46878f2b5fdadfbe062f9ed6d",
            services: {
                booth: "https://api.booth.pm",
                factory: "https:\/\/factory.pixiv.net\/",
                sketch: "https:\/\/sketch.pixiv.net",
        },



        isMobile: 
            false,
        oneSignalAppId:
            "b2af994d-2a00-40ba-b1fa-684491f6760a",
        publicPath: 
            "https:\/\/s.pximg.net\/www\/js\/spa\/",
        commonResourcePath: 
            "https:\/\/s.pximg.net\/common\/",
        development: 
            false,

        
        userData: {
            id: 
                "20929195",
            name: 
                "Shiina Orez",
            profileImg:
                "https:\/\/i.pximg.net\/user-profile\/img\/2017\/12\/04\/01\/26\/17\/13524847_e1adc4ab0054fbc4512ba4ceedd1bc1c_50.jpg",
            premium: 
                true,
            xRestrict: 
                2,
            adult: 
                true,
            },


        premium: {
            popularSearch: 
                true,
            novelCoverReupload: 
                true,
        },

        
        preload: {
            timestamp: 
                "2018-08-28T01:56:54+09:00",
            user: { 
                3016: {
                    "userId":
                        "3016",
                    "name":
                        "\u5c0f\u6797\u3061\u3055\u3068\u25a0\u30b3\u30df\u30b1\u304a\u75b2\u308c",
                    "image":
                        "https:\/\/i.pximg.net\/user-profile\/img\/2017\/02\/20\/05\/00\/11\/12173140_0fdfd80ae9dba9548e9bb47fed99768b_50.jpg",
                    "imageBig":
                        "https:\/\/i.pximg.net\/user-profile\/img\/2017\/02\/20\/05\/00\/11\/12173140_0fdfd80ae9dba9548e9bb47fed99768b_170.jpg",
                    "premium":
                        false,
                    "isFollowed":
                        true,
                    "background":
                        null,
                    "partial":
                        1,
                    "following":
                        304,
                    "followedBack":
                        false,
                    "comment":
                        "\u30b2\u30fc\u30e0\u30a4\u30e9\u30b9\u30c8\u30fb\u633f\u7d75\u30fb\u30ad\u30e3\u30e9\u30c7\u30fb\u305d\u306e\u4ed6\u30a4\u30e9\u30b9\u30c8\u5168\u822c\u3084\u3063\u3066\u307e\u3059\u3002\r\n\u5927\u9cf3\u3092\u5ac1\u306b\u3057\u305f\u4f50\u93ae\u63d0\u7763\u3001\u8352\u6f6e\u6539\u4e8c\u3068\u6d6e\u6c17\u3057\u3066\u308b\u3002\r\n\u4e09\u5ea6\u306e\u98ef\u3088\u308a\u7f8e\u811a\u304c\u597d\u304d\u8db3\u30d5\u30a7\u30c1\u3002\r\n\u30cb\u30b3\u30cb\u30b3\u25a0http:\/\/seiga.nicovideo.jp\/user\/illust\/1134053",
                    "commentHtml":
                        "\u30b2\u30fc\u30e0\u30a4\u30e9\u30b9\u30c8\u30fb\u633f\u7d75\u30fb\u30ad\u30e3\u30e9\u30c7\u30fb\u305d\u306e\u4ed6\u30a4\u30e9\u30b9\u30c8\u5168\u822c\u3084\u3063\u3066\u307e\u3059\u3002\u003Cbr \/\u003E\u5927\u9cf3\u3092\u5ac1\u306b\u3057\u305f\u4f50\u93ae\u63d0\u7763\u3001\u8352\u6f6e\u6539\u4e8c\u3068\u6d6e\u6c17\u3057\u3066\u308b\u3002\u003Cbr \/\u003E\u4e09\u5ea6\u306e\u98ef\u3088\u308a\u7f8e\u811a\u304c\u597d\u304d\u8db3\u30d5\u30a7\u30c1\u3002\u003Cbr \/\u003E\u30cb\u30b3\u30cb\u30b3\u25a0\u003Ca href=\u0022\/jump.php?http%3A%2F%2Fseiga.nicovideo.jp%2Fuser%2Fillust%2F1134053\u0022 target=\u0022_blank\u0022\u003Ehttp:\/\/seiga.nicovideo.jp\/user\/illust\/1134053\u003C\/a\u003E",
                    "webpage":
                        null,
                    "social":{
                        "twitter":{
                            "url":
                                "https:\/\/twitter.com\/pockyfactory"
                            },
                        "facebook":{
                            "url":
                                "https:\/\/www.facebook.com\/pockyfactory"
                            },
                        "circlems":{
                            "url":
                                "https:\/\/portal.circle.ms\/Circle\/Index\/10019833"
                            }
                        },
                    "region":{
                        "name":
                            "\u65e5\u672c",
                        "privacyLevel":
                            "0"
                        },
                    "birthDay":{
                        "name":
                            "4\u67084\u65e5",
                        "privacyLevel":
                            "0"
                        },
                    "gender":{
                        "name":
                            null,
                        "privacyLevel":
                            null
                        },
                    "job":{
                        "name":
                            "\u521b\u4f5c\u5173\u8054",
                        "privacyLevel":
                            "0"
                        },
                    "workspace":{
                        "userWorkspaceTool":
                            "PhotoshopCS4\u3001SAI",
                        "userWorkspaceMouse":
                            "USB"
                        },
                    "official":
                        false,
                    "group":
                        null
                    } 
                },
            },
            mute: 
                [],
        });
</script>"""

soup=BeautifulSoup(txt,'html.parser')

s=soup.find('script')
print(s.text)
'''print (s.get('token'))'''