[Meta Audience Network](/docs/audience-network)

  * [How To Use This Site](/docs/audience-network/how-to-use-this-site)
  * [Bidding Integration](/docs/audience-network/bidding-integration)
  * [Platform Setup](/docs/audience-network/setting-up/platform-setup)
  * [Ad Setup](/docs/audience-network/setting-up/ad-setup)
  * [Testing Your Setup](/docs/audience-network/setting-up/testing)
  * [Best Practices](/docs/audience-network/optimization/best-practices)
  * [APIs](/docs/audience-network/optimization/apis)
  * [Instant Games](/docs/audience-network/instant-games)
  * [Help](/docs/audience-network/support)

# Information for Child-Directed Apps and Services

When you participate in Meta Audience Network and use the Facebook SDKs in
apps or services that are directed to children, or where you knowingly collect
personal information from children, you are responsible for complying with all
applicable laws. For example, in the United States, operators of web sites,
apps or services that are directed to children under 13 or that knowingly
collect personal information from children under 13 must comply with the [U.S.
Children’s Online Privacy Protection Act
(“COPPA”).](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.business.ftc.gov%2Fprivacy-
and-
security%2Fchildren%2527s-privacy%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR0E0Vay6LoaG9lxitxMhmA514t69CmSKz8_AX94ElewSudttV5i5DPF1eg_aem_-
MVngzvxgGiupTY1vJKDaQ&h=AT320OXBtyrRDktY6JljowmGNbTPTwUBM3mS8i5owsR-
Wc_IXO1yiQ9xcjd7aEGKKV-
cPVljJTwJHat6-U9G6kopEQYZosWpjfMoQ3ako8SEN6Ekw4hNO1H501zehsrgBFge7JJcnIw)

Under the [COPPA
Rule](https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.ecfr.gov%2Fcgi-
bin%2Ftext-
idx%3FSID%3Ded5f76ab1e38b07607347f089c048eb8%26node%3Dse16.1.312_12%26rgn%3Ddiv8%26fbclid%3DIwZXh0bgNhZW0CMTEAAR1D2_zHFRs3cOSNnImc1yikTYzVM4zDorwZzkVxpEvrWsu6v1R-krM02TI_aem_TVWO0NvZSzYi66D5DToWNQ&h=AT0e5G26xStq_PiZUU5t-5ZYW-
ES-
OAmnAr7teBjo6niynwy6Lth1U22UDrkvCtHMaCsdpnszaGeCeAM7NAZYpUM_2E6P102AQtg8mjUKmsZEO5Ix_t-
xQRlcl3fXa2hF6BWTM4Dw9c) and per FTC guidance, developers are responsible for
determining whether or not an app is child directed by looking to “its subject
matter, visual content, use of animated characters or child-oriented
activities and incentives, music or other audio content, age of models,
presence of child celebrities or celebrities who appeal to children, language
or other characteristics of the Web site or online service, as well as whether
advertising promoting or appearing on the Web site or online service is
directed to children . . . [and] competent and reliable empirical evidence
regarding audience composition, and evidence regarding the intended audience.”

If the app is child directed and children under the age of 13 are the primary
audience, then it is “primarily child directed.”

Apps that are child directed, but do not target children as the primary
audience, are “child directed, but mixed audience” services under the COPPA
Rule. If an app is child directed but mixed audience, it can choose to
implement an age gate, a mechanism that asks users to provide their age or
date of birth in an age-neutral way. Child directed, but mixed audience apps
that implement age gates are permitted to differentiate among users for
purposes of COPPA compliance.

This document provides the additional code you are required to use for the
Facebook SDKs if you have determined that your site, app, or service has
obligations under COPPA. Where you use this code depends on your determination
of which of the following categories applies to your site, app, or service.

  1. [Primarily child-directed](/docs/plugins/restrictions#child-directed). Your site, app, or service is [directed to children](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR11_X7uOWmClLEDKaEAltXqcXuMY2iY0v0MPvSrhQ4y3tALI12fhaH-67M_aem__8qBIZXmTCxwQBmqrzFeJw&h=AT1Xbj9ZB8jS87LHjgx1GXyJ4NXTu9kKHbKxuFAGRYnaSUhuVO4mwv_1ArWlnQNUU8zeetNJoN3tR_JKjbiUCNvS3YoW6Fj3sH3DAaIJv0ccq7qA6VT8Uidquezmi2ncy9ncJ0rUEm0) whose primary target audience is children under the age of 13. 
  2. [Mixed audience without age gate](/docs/plugins/restrictions#mixed-no-age-gate). Your site, app, or service is [directed to children](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR1L_JhlqFrN-PxZvg7X1TnVBYLlE98xDhW3hsOKgEngHYnF72hefKYFiAY_aem_YLiRMns8xHhAcPdqhTNAmQ&h=AT2FCxzT1SLjoftLd4qUzGpBXtIWDnQzwnxJiMjSxlHWZzuA3uzcH0BQ434yrrlhH3zwvOBAxwTREBaxjgIfCTew167t7K01ZkAEU3MHbeysAyZNyqOjFE0QYRvfxbGNledyg4rlO64) but its primary target audience is people who are at least 13 years old. Your site, app or service does not include an age gate. An “age gate” generally is a mechanism that asks users to provide their age or date of birth in a non-leading way before they access a website or service. For more information [click here](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR2fc2Ww0ru_JEmR1CbYNBdrJ5PWi7IDLl59NeJgkZ95JlpRwHeDVT_fq3w_aem_KAv5iN-XbqjcQgBFFOxCpA&h=AT0smBVOxgAy1sKanfmQ_LQTaQdV9DNWr2FDJxm8QaG9kGWhOwtoGvpIh1_IOkquzlDZ3SkkthfhSDG9KIUMeDmg0o-0ZDI7ClbXs3VYRFIAraHbWLwTVZz1XQt4byl7WoSQagm-nXo).
  3. [Mixed audience with age gate](/docs/plugins/restrictions#mixed-with-age-gate). Your site, app, or service is [directed to children](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR2C7BIA83CjsamVgArYJZF1ZvH1xTvkgSEQp0EgAGVlkhyUSlTN98T38s4_aem_wG11XviEuGBjNCND7aW2vw&h=AT1woZJPAC0x3A8AVVBiix65PLFyvNLRs03B5-Wqv7KlSH3u0-EngfEv8PcHZJIdeD-9uYjAYVZxhB3KL-jgHeS5VwhKhCXBe39YsZqu6WsHuEqQxhz-7S-cvIWRuDAQ6Zgh7SR1CEk) but its primary target audience is people who are at least 13 years old. Your site, app or service uses an age gate. An “age gate” generally is a mechanism that asks users to provide their age or date of birth in a non-leading way before they access a website or service. For more information [click here](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR11Doj2ky65-E5KaOTBxOgYFTejWpiQiyq5W7K7KQXjUqIqopOq2789NZ4_aem_D2-KTtPP3v78NS5j1su-vg&h=AT1w2jUSubBrKkIdmbuP-LcyxQPmo5smJEzl1vulLcLnJrcaqL26ADciEiV2IWykMmiBYBJIvcrRCDADe71OPxr81ZW2q0XKR9cW0lTh1fsJBBFUdeP7aLC6STcaImBCGM6ibJTSnkE).

If your app or service is **Primarily Child-Directed** , then you may not use
the Facebook Audience Network SDKs.

If your app or service is **Mixed Audience without an Age Gate** , then you
may use the Facebook Audience Network SDKs only if you set the
`setMixedAudience` flag for all users. When an app or service tells Facebook
that the `setMixedAudience` flag is set in the Audience Network SDK, Facebook
will only serve ads to non-United States users of that app through the
Audience Network services.

◦ iOS:
<https://developers.facebook.com/docs/reference/ios/4.6/class/FBAdSettings/>

◦ Android:
[https://developers.facebook.com/docs/reference/android/current/class/AdSettings/#setMixedAudience](/docs/reference/android/current/class/AdSettings/#setMixedAudience)

For apps or services that are **Mixed Audience with an Age Gate** and where an
individual user represents that they are under 13, you may not issue an ad
request to the Audience Network by ensuring that the Audience Network is not
being requested in your view controller (iOS), activity class (Android), or
any respective app function. Where an individual represents that they are at
least 13 years old, you may use the Audience Network SDK without setting the
`setMixedAudience` flag.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1668333663438923&ev=PageView&noscript=1)

``

``

``

``

