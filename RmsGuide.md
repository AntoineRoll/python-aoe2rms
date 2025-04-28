Age of Empires II

Definitive Random Map Scripting Guide

[CLICK HERE](https://www.google.com/url?q=https://docs.google.com/document/d/e/2PACX-1vR_I1I9u-hI2FFm-EYyjoM_-9dNJFOfTaIgr05wXNbdpv9tI18b6r18ARULy3Jqyvlq6-lc2VjX6xP4/pub&sa=D&source=editors&ust=1744981493165940&usg=AOvVaw2RYKK7XMNFUXmxzBDNrhp0) for a lightweight read-only version

[CLICK HERE](https://www.google.com/url?q=https://docs.google.com/document/d/1jnhZXoeL9mkRUJxcGlKnO98fIwFKStP_OBozpr0CHXo/&sa=D&source=editors&ust=1744981493166253&usg=AOvVaw1vAmjBZGP6cjJh5zIWyGnK) for the version with a full document outline (also read-only; but you may request edit access)

# Table of Contents

[Introduction](#h.rr6es6hjib6k)

[Syntax Overview](#h.n7e599qykcgh)

[Syntax Skeleton](#h.wk54iauf6a3w)

        [PLAYER\_SETUP](#h.1jv1nmqnml7h)

        [LAND\_GENERATION](#h.15g4dj26anlp)

        [ELEVATION\_GENERATION](#h.szmawgkuqtsf)

        [CLIFF\_GENERATION](#h.gi5bya8szfbw)

        [TERRAIN\_GENERATION](#h.2mwmqwe7m0vw)

        [CONNECTION\_GENERATION](#h.urxh5ze1aaoh)

        [OBJECTS\_GENERATION](#h.unkzqmnnqr5v)

        [Global Syntax](#h.bacsucwqlnyd)

        [Random Code](#h.87mv66lnefdm)

        [Conditionals](#h.vs551a7tyxet)

        [Map Sizes](#h.qannz915qgy5)

        [Walls](#h.q7o6xdvi0noo)

[Constant Reference](#h.9iqqcke3biv)

        [Terrains](#h.3bdjnf7tryyk)

        [Objects](#h.nvxriamulybh)

        [Effects](#h.90ed1yz7qe0h)

        [Attributes](#h.oumcl095iabt)

        [Resources](#h.cym0hd55425r)

        [Technologies](#h.eo6nl4huxzuz)

        [Classes](#h.lvcoxxnz995p)

        [Miscellaneous](#h.2n1q8vynhc9o)

[Scripting and Testing](#h.8flmgbdpty4t)

        [Standard Units and Resources](#h.umeodbvqve7n)

        [Game Mode Support](#h.nlz2m8jsu3b0)

        [Testing](#h.nzu22x6f9z5i)

        [Publishing a Map](#h.spl4nv9kuyt9)

        [Updating an Old Map for DE](#h.4pjjlakdsv1)

[Links and Resources](#h.toi7hmld9en6)

        [Videos](#h.id1m7it9fp54)

        [General Guides](#h.osnx86rj6196)

        [Example Scripts](#h.evri4pvhyl)

        [Syntax Highlighting](#h.rxbtnzoqa78k)

[Appendix](#h.2hnbx3yhbq7g)

        [DE Update Bulletin](#h.mlxyendnzikn)

# Introduction

## Foreword

This guide is a comprehensive documentation of random map scripting in Age of Empires 2.  It was written after the release of the Definitive Edition, but is relevant for all older versions of AoE2 as well.  It is updated regularly, especially after the Definitive Edition adds new features to random map scripting.

If you notice typos, mistakes, inaccuracies, dead links, etc. or you have comments, suggestions or additions, contact me (on Discord) and I can fix the issue or give you commenting or editing permissions.

Come join the Random Map [Discord](https://www.google.com/url?q=https://discord.gg/a4n3zt5EST&sa=D&source=editors&ust=1744981493170579&usg=AOvVaw1uKl6bd6wFbYKPU2QSm6cs) to chat with other map scripters!

Have fun map scripting!  ~Zetnus

## What is an RMS?

RMS stands for Random Map Script.  An RMS is what the game uses to randomly generate maps (such as Arabia or Black Forest).  Random Map Scripts are NOT scenarios and are NOT produced in the in-game editor (but they can be generated and tested in the editor).  They look different every time.  They are plain text files (with the extension .rms) and are made in any text editor (like Notepad).  Just click "save as" and type .rms as the extension.  The community has made RMS syntax highlighters for numerous common text editors (see the [Syntax Highlighting](#h.rxbtnzoqa78k) section at the end of this guide).

## How to choose an RMS in-game

To use a custom random map, you need to look under "random map", not in your scenarios list.  Change the "map style" to "custom" and then pick the map.  You can also choose a custom RMS and generate it in the scenario editor to see what it can look like.

## Game Versions

Age of Empires 2 has received numerous expansions, has been re-released twice, and also has community-made patches.  In order to prevent confusion, let us briefly look at these versions and what they mean for random map scripting.

[Age of Kings](https://www.google.com/url?q=https://www.amazon.com/Age-Empires-2-Kings-PC/dp/B00002NDRY&sa=D&source=editors&ust=1744981493172638&usg=AOvVaw2KQPQV4V1HVCRiHtd6Acfn) (1999) (AoK) - The first release.  Did not support custom random map scripts.  Not played anymore, although you still can play it if you get the CD.

[Age of Conquerors](https://www.google.com/url?q=https://www.amazon.com/Age-Empires-II-Gold-PC/dp/B00005N9A7&sa=D&source=editors&ust=1744981493173043&usg=AOvVaw0Rh6mt3JthCLnICF17w-Si) (2000) (AoC) - Expansion to AoK.  Supported custom random map scripts.  Also referred to as the CD version of the game.  Played for many years and you can still play multiplayer on [GameRanger](https://www.google.com/url?q=http://www.gameranger.com/&sa=D&source=editors&ust=1744981493173384&usg=AOvVaw1mJ57vz810keVIZABgTfxS).

[UserPatch](https://www.google.com/url?q=http://userpatch.aiscripters.net/&sa=D&source=editors&ust=1744981493173534&usg=AOvVaw2DHjdGpD2EAphW2iUFCvXe) (UP) - Community-made quality-of-life update for AoC.  Currently on version 1.5.  Originates in the AI scripting community, but also brings many new features to RM scripting.  Used as the basis for multiplayer on [Voobly](https://www.google.com/url?q=https://www.voobly.com/&sa=D&source=editors&ust=1744981493173884&usg=AOvVaw3g1klU-CNWb4CPL80aOk6U).

[HD Edition](https://www.google.com/url?q=https://store.steampowered.com/app/221380/Age_of_Empires_II_2013/&sa=D&source=editors&ust=1744981493174064&usg=AOvVaw0iobtQ1KYyaT1gUeKOGgW6) (2013) (HD) - Re-release of AoC on the Steam platform.  Eventually implemented most RMS features from UP1.4 (but not from 1.5).  Received 3 downloadable content (DLC) expansions, namely:

[The Forgotten](https://www.google.com/url?q=https://store.steampowered.com/app/239550/Age_of_Empires_II_2013_The_Forgotten/&sa=D&source=editors&ust=1744981493174449&usg=AOvVaw09WFUmNkggOz5tEnf0vMuB) (AoF) - A fan-made expansion turned official.

[African Kingdoms](https://www.google.com/url?q=https://store.steampowered.com/app/355950/Age_of_Empires_II_2013_The_African_Kingdoms/&sa=D&source=editors&ust=1744981493174684&usg=AOvVaw0KboOD5ce-nvnpJLt6kK-R) - Content centered around Africa.

[Rise of the Rajas](https://www.google.com/url?q=https://store.steampowered.com/app/488060/Age_of_Empires_II_2013_Rise_of_the_Rajas/&sa=D&source=editors&ust=1744981493174912&usg=AOvVaw3VrqqyMVUxqPYSYkuuJNs_) - Content centered around south-east Asia.

[WololoKingdoms](https://www.google.com/url?q=https://github.com/Jineapple/WololoKingdoms/releases&sa=D&source=editors&ust=1744981493175113&usg=AOvVaw0shyY2Z2DOC7nUuxLedCD4) (WK) - A fan-made mod for AoC running on UP1.5 that adds all DLC objects from the HD Edition and allows it to be used for multiplayer on [Voobly](https://www.google.com/url?q=https://www.voobly.com/&sa=D&source=editors&ust=1744981493175336&usg=AOvVaw1qihelXol3yFNjlA32AhbZ).

[Definitive Edition](https://www.google.com/url?q=https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/&sa=D&source=editors&ust=1744981493175493&usg=AOvVaw2F1G2ebj4NW75xzyOhuztr) (2019) (DE) - Remaster of the game, including all previous expansions. Implements most UP1.5 features, and adds many new features.  Most of the RMS community now makes maps for DE.  DE has several expansions adding more civilizations and campaigns, but owning them is not required to use their new objects in RMS. Received several DLC expansions so far:

[Lords of the West](https://www.google.com/url?q=https://store.steampowered.com/app/1389240/Age_of_Empires_II_Definitive_Edition__Lords_of_the_West/&sa=D&source=editors&ust=1744981493176017&usg=AOvVaw0GGMbUgCHTyDrQ1VHbYodk) - Adds Burgundians and Sicilians.

[Dawn of the Dukes](https://www.google.com/url?q=https://store.steampowered.com/app/1557210/Age_of_Empires_II_Definitive_Edition__Dawn_of_the_Dukes/&sa=D&source=editors&ust=1744981493176250&usg=AOvVaw2Gktlt0FsCcOy_Pw5AJueB) - Adds Bohemians and Poles.

[Dynasties of India](https://www.google.com/url?q=https://store.steampowered.com/app/1869820/Age_of_Empires_II_Definitive_Edition__Dynasties_of_India/&sa=D&source=editors&ust=1744981493176447&usg=AOvVaw3NGlKUJwnU1zkpoQUJs3rt) - Splits the former Indians civilization into 4 new civs.

[Return of Rome](https://www.google.com/url?q=https://store.steampowered.com/app/2141580/Age_of_Empires_II_Definitive_Edition__Return_of_Rome/&sa=D&source=editors&ust=1744981493176688&usg=AOvVaw3fL3anUNW4OgNQOEFYORJX) - Adds the Romans to AoE2.  Also adds AoE1 into the AoE2 engine and game, which gives AoE1 custom random map script support.

[The Mountain Royals](https://www.google.com/url?q=https://store.steampowered.com/app/2555420/Age_of_Empires_II_Definitive_Edition__The_Mountain_Royals/&sa=D&source=editors&ust=1744981493176996&usg=AOvVaw2KWzyFM6TUgW-DOLI1xd6A) - Adds Georgians and Armenians.

## Where to put a manually downloaded RMS

If you manually download a custom RMS (rather than subscribing directly to a mod) you will need to manually place it in the correct place.  This varies by game version.

* In DE, maps can be in a subfolder and will be grouped with other maps in that subfolder.

AoC:

Microsoft Games\Age of Empires II\Random

HD:

Steam\SteamApps\common\Age2HD\resources\\_common\random-map-scripts

DE (Steam):
Steam\SteamApps\common\Aoe2DE\resources\\_common\random-map-scripts

or:

Users\[WindowsUsername]\Games\Age of Empires 2 DE\[UserID]\resources\\_common\random-map-scripts

* This folder does not exist by default, so you must first create it.

DE (Microsoft Store):

Users\[WindowsUsername]\Games\Age of Empires 2 DE\[UserID]\resources\\_common\random-map-scripts

* This folder does not exist by default, so you must first create it.

WK (local):

Microsoft Games\Age of Empires II\Games\WololoKingdoms\Script.Rm

WK (Voobly):

Microsoft Games\Age of Empires II\Voobly Mods\AOC\Data Mods\WololoKingdoms\Script.Rm

HD + Voobly (using the[Compatibility Patch](https://www.google.com/url?q=http://aoccs.net/&sa=D&source=editors&ust=1744981493179437&usg=AOvVaw08zaSf04-63-Sk0PvN37_i)):

Steam\steamapps\common\Age2HD\Random

HD + Voobly + WK:

Steam\steamapps\common\Age2HD\Voobly Mods\AOC\Data Mods\WololoKingdoms\Script.Rm

## Where to find the Standard Random Map Scripts

You might want to look at the standard map scripts, to see what they do, and how they do it.

AoC: Age of Empires II\Data\gamedata\_x1.drs

You can open the drs file with any text editor.  It will display a whole bunch of junk characters, but the map scripts are also there, so you can take a look or copy them into another file.

HD: Age2HD\resources\\_common\drs\gamedata\_x1 and Age2HD\resources\\_common\drs\gamedata\_x2

The scripts are there as \*.rms files.  The \_x1 folder contains the AoC versions of the scripts and is used when playing with the basegame dataset in HD.  The \_x2 folder contains the updated versions, with DLC objects.

DE (Steam): AoE2DE\resources\\_common\drs\gamedata\_x2

Note that you must create a separate renamed copy if you want to edit the official maps.

DE (Microsoft Store):

You can run the game and then open AoE2DE's process location by right-clicking it in the Task Manager's Details. The actual game folder and its subfolders are readable at all times (no need to take ownership), the parent folder (WindowsApps) is the one that is unreadable.

WK (local): Age of Empires II\Games\WololoKingdoms\Data\gamedata\_x1.drs

You can open the drs file with any text editor.  It will display a whole bunch of junk characters, but the map scripts are also there, so you can take a look or copy them into another file.

Any (local) UserPatch mod: Age of Empires II\Games\ModName\Data\gamedata\_x1.drs

You can open the drs file with any text editor.  It will display a whole bunch of junk characters, but the map scripts are also there, so you can take a look or copy them into another file.

## Getting Started

This guide is long, and reads more like a reference or a documentation of everything that is possible, rather than as an easy introduction for beginners.  If you are completely new to random map scripting it might be easier to find an existing map and take a look at the script to tweak it to observe the changes.

I can also recommend taking a look [TheMadCADer's YouTube playlist](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DFk9Sc6YqHFw%26list%3DPLYYZYNnmocy0XrBC1m1xj1__xRoOri8G5&sa=D&source=editors&ust=1744981493184106&usg=AOvVaw0aFQgG5GzuysJNMXMr5PBs)

If you want example scripts to look at and modify, take a look at [Example Scripts](#h.evri4pvhyl).

(I do NOT recommend using the official map scripts in DE to learn, especially not those that are based on tournament maps/versions.  The DE official Arabia script and any of the Red Bull Wololo maps are very complex.)

A quick overview of some important sections in this guide:

[Syntax Skeleton](#h.wk54iauf6a3w) - lists every possible command and attribute, along with default values, a description and an example.  Refer to it when you are unsure about the usage of a command.

[Random Code](#h.87mv66lnefdm) and [Conditionals](#h.vs551a7tyxet) - read these sections so that you understand how to vary things in your map.

[Constants](#h.yy17pxjmocyk) and [Constant Reference](#h.9iqqcke3biv) - learn how to use terrains and objects that do not have a pre-defined name.

[Testing](#h.nzu22x6f9z5i) and [Publishing a Map](#h.spl4nv9kuyt9) - learn how to efficiently test your map and how to properly upload it.

[Links and Resources](#h.toi7hmld9en6) - a list of external things that might be worth looking at, and also the place to pick up an RMS syntax highlighter.

---

#

# Syntax Overview

A random map script contains up to seven different sections.

This is the order in which the game will use sections to generate the map:

[<PLAYER\_SETUP>](#h.1jv1nmqnml7h)   Determine player placement and modify things in the gamedata

[<LAND\_GENERATION>](#h.15g4dj26anlp)   Place main landmasses of terrain

[<ELEVATION\_GENERATION>](#h.szmawgkuqtsf)   Create hills

[<CLIFF\_GENERATION>](#h.gi5bya8szfbw)   Create cliffs

[<TERRAIN\_GENERATION>](#h.2mwmqwe7m0vw)   Replace terrains with other terrains

[<CONNECTION\_GENERATION>](#h.urxh5ze1aaoh)   Replace terrains between players and/or lands

[<OBJECTS\_GENERATION>](#h.unkzqmnnqr5v)   Place units, buildings, resources, etc.

.

* The sections can be written in any order, but the game uses them in the order above.

* The official scripts are not written in the "correct" order.

* Not all sections are necessary.

* If you don’t want cliffs, don’t include <CLIFF\_GENERATION>

* You can have multiple sections of the same type.  They should function identically to a single section.

Each section has different commands that can be used in it.  Many commands have attributes that can be used to modify the commands from their defaults.  There is also global syntax that can be used anywhere in your script (including outside of sections).

* You can use indentations, spaces, tabs, newlines freely in whichever way helps readability the most - they are all recognized as separators.  You could write the entire script in one line and it would still work.  Just make sure everything is separated by some sort of separator.
* The rms parser is very robust.  It will ignore things it cannot interpret or cannot place and still move on.
* Syntax is case-sensitive.
* Commands and attributes are usually processed in the order they appear within their section.
* Attributes are contained in curly brackets. The brackets don't have to be on a new line, but they often are written that way.  Attributes don't have to be indented, but it helps readability if they are.  Example:

command

{

attribute

attribute2 argument

}

* For the examples in the guide, I will generally use a more compact notation to save space:

command {

attribute

attribute2 argument

}

* One can also use even more compact notation by leaving out newlines entirely:
          command { attribute attribute2 argument }
* Most attributes are optional; you can leave out an attribute and it will use its default value.
* Attribute order within a command generally does not matter; however, if you duplicate an attribute or use mutually exclusive attributes, the final one will apply.
* Some commands and attributes have arguments - either numeric values or identifiers associated with terrains and objects.
* The parser only uses integers (whole numbers); if you use a decimal, it will ignore everything past the decimal point (or comma, or any other non-numeric character).
* Negative numbers can be used, but it only makes sense to do so for some arguments.
* In UP and DE, [rnd(min,max)](#h.ml72cdygzrfv) can be used instead of a numeric argument to pick a random number between min and max (inclusive).  Make sure not to include any spaces in the whole construct!
* If you specify an identifier that is not defined, the parser ignores it and keeps going (or substitutes the most recent valid identifier).
* Not all commands and attributes work in all versions of the game - check the description in the syntax reference section!
* You can use a maximum of 100000 create\_ commands per section.  Commands that are in not-chosen logical branches do not contribute to the limit when not chosen.  In all versions prior to DE, this limit is only 99.

---

##

# Syntax Skeleton

This section shows all the possible syntax, so you can see which attributes and commands are available.  It also acts as a table of contents.  Explanations are in the next chapter.

Arguments are listed as follows:

* N refers to a number.
* % refers to a number (usually in the range 0-100).
* TYPE refers to a constant identifier.
* CONDITION refers to something which you expect to sometimes be true and sometimes be false; it might be a game setting, or even something you define yourself!
* FILENAME refers to an external file to be loaded.
* / means that there are multiple possible commands or attributes to choose from.  In some cases (but not all), these may be mutually exclusive.

[<PLAYER\_SETUP>](#h.1jv1nmqnml7h)

[random\_placement](#h.l4ykw7wa466e) / [grouped\_by\_team](#h.31ppsgfv9i7y) / [direct\_placement](#h.jbnjt99zhiqx)

[nomad\_resources](#h.fj85jt1i1f2l)

[force\_nomad\_treaty](#h.13why2qs1rix)

[behavior\_version N](#h.seeuqpcozayb)

[override\_map\_size N](#h.sdzu3ermj1ah)

[set\_gaia\_civilization N](#h.yy69o1bqyfx5)

[ai\_info\_map\_type TYPE N N N](#h.6o9sfjx8tww0)

[effect\_amount TYPE TYPE TYPE N](#h.1niw1edwqhy5)

[effect\_percent TYPE TYPE TYPE %](#h.7siepjsm3bdc)

[guard\_state TYPE TYPE N N](#h.7jvxo0vqwqu8)

[terrain\_state N N N N](#h.tdph3oglggjk)

[weather\_type N N N N](#h.ht15fzasksgc)

[<LAND\_GENERATION>](#h.15g4dj26anlp)

[base\_terrain TYPE](#h.t4mfjnozvxwf)

[base\_layer TYPE](#h.p6oqwj1l7flh)

[enable\_waves N](#h.fno7myp7722j)

[create\_player\_lands](#h.esy5dq29i0wr)

{

        [terrain\_type TYPE](#h.lzceesmva36o)

        [land\_percent %](#h.ipg3ruf70nn4) / [number\_of\_tiles N](#h.bzvr6x5i10na)

        [base\_size N](#h.b9qafcmyygh)

        [circle\_radius % N](#h.lc3eipzhfx0z)

        [left\_border %](#h.xrncn5cs75or)

        [right\_border %](#h.h0hz0dquv1vc)

        [top\_border %](#h.7oog42u9uwjn)

        [bottom\_border %](#h.mwha0mo8ve9s)

        [border\_fuzziness %](#h.ibpssq2wln80)

        [clumping\_factor N](#h.7e3knrokkcni)

        [base\_elevation N](#h.ppqecxdcopxb)

        [zone N](#h.li85mvsiskop) / [set\_zone\_by\_team](#h.6pxlle5x8e8w) / [set\_zone\_randomly](#h.nweca22q5puk)

        [other\_zone\_avoidance\_distance N](#h.2oebaei6j04a)

        [land\_id N](#h.c97q6t5q24lj)

}

[create\_land](#h.te4jg2upqvlx)

{

        [terrain\_type TYPE](#h.lzceesmva36o)

        [land\_percent %](#h.ipg3ruf70nn4) / [number\_of\_tiles N](#h.bzvr6x5i10na)

        [base\_size N](#h.b9qafcmyygh)

        [land\_position % %](#h.fnezpf6c85yf)

        [left\_border %](#h.xrncn5cs75or)

        [right\_border %](#h.h0hz0dquv1vc)

        [top\_border %](#h.7oog42u9uwjn)

        [bottom\_border %](#h.mwha0mo8ve9s)

        [border\_fuzziness %](#h.ibpssq2wln80)

        [clumping\_factor N](#h.7e3knrokkcni)

        [base\_elevation N](#h.ppqecxdcopxb)

        [assign\_to\_player N](#h.mok24wym6kiz) / [assign\_to TYPE N N N](#h.b6uul7n11c6g)

        [zone N](#h.li85mvsiskop) / [set\_zone\_randomly](#h.nweca22q5puk)

        [other\_zone\_avoidance\_distance N](#h.2oebaei6j04a)

        [min\_placement\_distance N](#h.6d0lk4yitd95)

        [land\_id N](#h.c97q6t5q24lj)

}

[<ELEVATION\_GENERATION>](#h.szmawgkuqtsf)

[create\_elevation N](#h.h85o0pyielaj)

{

        [base\_terrain TYPE](#h.y6zq54jntrkn)

        [base\_layer TYPE](#h.my6smlk88r2j)

        [number\_of\_tiles N](#h.efs6lqjf3k0x)

        [number\_of\_clumps N](#h.7u0osqxg1v3m)

        [set\_scale\_by\_size](#h.8vbd2ko0sw7f) / [set\_scale\_by\_groups](#h.3vkc0lxd4r4a)

        [spacing N](#h.hqjpcx4o099o)

        [enable\_balanced\_elevation](#h.izx21xcrwjlg)

}

[<CLIFF\_GENERATION>](#h.gi5bya8szfbw)

[cliff\_type TYPE](#h.ydwb5bkkiqmi)

[min\_number\_of\_cliffs N](#h.3j0rxjupzp29)

[max\_number\_of\_cliffs N](#h.fd5g85qqk5wj)

[min\_length\_of\_cliff N](#h.58mxeqmbhw5c)

[max\_length\_of\_cliff N](#h.1ee8y599eivc)

[cliff\_curliness %](#h.6ns6xzfo7h7c)

[min\_distance\_cliffs N](#h.sj0nz9h7pbsy)

[min\_terrain\_distance N](#h.gorf7iar00tm)

[<TERRAIN\_GENERATION>](#h.2mwmqwe7m0vw)

[color\_correction TYPE](#h.7xt01aajnkw9)

[create\_terrain TYPE](#h.acnibljecbfg)

{

        [base\_terrain TYPE](#h.ptxp1ht2fh0p)

        [base\_layer TYPE](#h.nlwld8oca536)

        [beach\_terrain TYPE](#h.qlmjwkuqe8hc)

        [terrain\_mask N](#h.e0ug99qovffm)

        [spacing\_to\_other\_terrain\_types N](#h.dzdzen1yp2wx)

        [set\_flat\_terrain\_only](#h.4300mvgw1xz7)

        [land\_percent %](#h.tzpfzbf2ze3w) / [number\_of\_tiles N](#h.qdz0o9mtb2hi)

        [number\_of\_clumps N](#h.1tzwe1brcw80)

        [clumping\_factor N](#h.mztseaf6qfgt)

        [set\_scale\_by\_size](#h.g4zvtvsbcm29) / [set\_scale\_by\_groups](#h.cl6w98j0bs9h)

        [set\_avoid\_player\_start\_areas N](#h.ijxhxwahit2u)

        [height\_limits N N](#h.oezholffksgg)

}

[<CONNECTION\_GENERATION>](#h.urxh5ze1aaoh)

[accumulate\_connections](#h.bd2l5930vfzf)

[create\_connect\_all\_players\_land](#h.br9ypglw81m2) / [create\_connect\_teams\_lands](#h.sbxghl4uf1bm) / [create\_connect\_all\_lands](#h.wm3xy9f5nbd9) / [create\_connect\_same\_land\_zones](#h.j1cvlkhvgxr4) / [create\_connect\_to\_nonplayer\_land](#h.ypcxynpvljp0)

{

        [default\_terrain\_replacement TYPE](#h.p16vd5cszmhm)

        [replace\_terrain TYPE TYPE](#h.5h9ggnuativl)

        [terrain\_cost TYPE N](#h.pw0ckpmic7kh)

        [terrain\_size TYPE N N](#h.o6c6lz9vb2w7)

}

[<OBJECTS\_GENERATION>](#h.unkzqmnnqr5v)

[create\_actor\_area N N N N](#h.u28jmnfojke3)

[create\_object TYPE](#h.2vz7nxt2afqo)

{

        [number\_of\_objects N](#h.btcx5h61er65)

        [number\_of\_groups N](#h.t7eg3wg2xm3w)

        [group\_variance N](#h.u5a62pn5z0hm)

        [group\_placement\_radius](#h.675xoyq748tw)

        [set\_tight\_grouping](#h.ksq6iglmnili) / [set\_loose\_grouping](#h.umboa0q57v9y)

        [min\_connected\_tiles N](#h.6rc3lgpd171k)

        [resource\_delta N](#h.ndaw6icg9cnp)

        [second\_object TYPE](#h.cr71z3stu8pd)

        [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6) / [set\_scaling\_to\_player\_number](#h.l48a16uing0q)

        [set\_place\_for\_every\_player](#h.hch89ipgsvb) / [place\_on\_specific\_land\_id N](#h.34wzlujx4lbv)

        [generate\_for\_first\_land\_only](#h.c3yp8xxihcnd)

        [set\_gaia\_object\_only](#h.bnzkfqaopnv9)

        [set\_gaia\_unconvertible](#h.g4mzdyb4izbo) / [set\_building\_capturable](#h.svu8loj25dpl)

        [make\_indestructible](#h.a9ken9hkekd6)

        [min\_distance\_to\_players N](#h.asuv2zzhmbsd)

        [max\_distance\_to\_players N](#h.v2aq68odkdzl)

        [set\_circular\_placement](#h.15fez3e52vqr)

        [terrain\_to\_place\_on TYPE](#h.t7m0dcvh1px)

        [layer\_to\_place\_on TYPE](#h.ze7b3ms0whcu)

        [ignore\_terrain\_restrictions](#h.fx1jh8glz0tl)

        [max\_distance\_to\_other\_zones N](#h.qf90qwpxyzrs)

        [place\_on\_forest\_zone](#h.38vodsu87lbp) / [avoid\_forest\_zone N](#h.ym7v1j9vbnle)

        [avoid\_cliff\_zone N](#h.t2916w9l2cff)

        [min\_distance\_to\_map\_edge N](#h.w2q69orjs3l3)

        [min\_distance\_group\_placement N](#h.b2u5jna014lf)

        [temp\_min\_distance\_group\_placement N](#h.a5n8aue3ffi4)

        [find\_closest](#h.kzkb7o2yhtk9)

        [find\_closest\_to\_map\_center](#h.c8jwpxwfx68p)

        [find\_closest\_to\_map\_edge](#h.mmr1mgkocjlx)

        [require\_path N](#h.woysch92a2oh)

        [force\_placement](#h.138scj5wa7v7)

        [actor\_area N](#h.obv5ypy66a57)

        [actor\_area\_radius N](#h.z9i7h4jrjeaf)

        [override\_actor\_radius\_if\_required](#h.4t8s9kqehrvb)

        [actor\_area\_to\_place\_in N](#h.d6d6k8uc57zx)

        [avoid\_actor\_area N](#h.cgoa0e8x398u)

        [avoid\_all\_actor\_areas](#h.5c5n6srms81p)

        [enable\_tile\_shuffling](#h.ewsg05tiznb0)

        [set\_facet N](#h.qbzrlsoh7lg7)

        [match\_player\_civ](#h.32nz9uxvp2kz)

}

/\* [global syntax](#h.bacsucwqlnyd) \*/

/\* [comment](#h.2knaho4i0qpg) \*/

[#include\_drs FILENAME](#h.qn6gojo7i9nv)

[#includeXS FILENAME](#h.w4knc4t4en6w)

[start\_random](#h.pyiuk8a7kiga)

        [percent\_chance %](#h.10ifrywpiesx)

[end\_random](#h.10ifrywpiesx)

[rnd(N,N)](#h.ml72cdygzrfv)

[if CONDITION](#h.w2egae5vfwo0)

[elseif](#h.w2egae5vfwo0)[CONDITION](#h.w2egae5vfwo0)

[else](#h.w2egae5vfwo0)

[endif](#h.w2egae5vfwo0)

[#define CONDITION](#h.hhofpn9iwfxi)

[#const TYPE N](#h.poaiyxi48mi6)

---

#

# Syntax Reference

## <PLAYER\_SETUP>

Default: [random\_placement](#h.l4ykw7wa466e)

Required section.  Determines how players will be placed, and modifies global parameters.

### random\_placement

Game versions: All

Mutually exclusive with: [grouped\_by\_team](#h.31ppsgfv9i7y)

Players are positioned in a circle with some variation.  This is the default, and will apply even if you do not type it.

Example:

<PLAYER\_SETUP>

random\_placement

### grouped\_by\_team

Game versions: UP/HD/DE

Mutually exclusive with: [random\_placement](#h.l4ykw7wa466e)

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493212945&usg=AOvVaw2CRTuSSbBKuZQ7sPHVe4u_)

Requires: [Team Together](#h.vs551a7tyxet) box ticked in the lobby (on by default)

Players of the same team are positioned in close proximity to each other.  Distance between team members is double the [base\_size](#h.b9qafcmyygh) used in [create\_player\_lands](#h.esy5dq29i0wr).

Example:

<PLAYER\_SETUP>

grouped\_by\_team

### direct\_placement

Game versions: UP/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493214110&usg=AOvVaw2qhqW4zhPVDyZBg1kQNOzk)

Allows the [land\_position](#h.fnezpf6c85yf) attribute in [create\_land](#h.te4jg2upqvlx) to be used in combination with the [assign\_to\_player](#h.mok24wym6kiz) or [assign\_to](#h.b6uul7n11c6g) attributes to individually position players at exact positions on the map.

* On UP, !P will be appended to the map name in the objectives window.
* On UP, it can be used in combination with [random\_placement](#h.l4ykw7wa466e) / [grouped\_by\_team](#h.31ppsgfv9i7y) but it only works when using [land\_position](#h.fnezpf6c85yf)
* On DE, it disables [random\_placement](#h.l4ykw7wa466e) and [grouped\_by\_team](#h.31ppsgfv9i7y), but doesn't necessarily require [land\_position](#h.fnezpf6c85yf) - it is possible to just specify borders instead.  If used with [create\_player\_lands](#h.esy5dq29i0wr), these lands will be positioned entirely at random (ignoring the normal circular positioning), so this is usually not desirable.

Example: Directly place player 1 at the center of the map (50%, 50%).

<PLAYER\_SETUP>

direct\_placement

<LAND\_GENERATION>

create\_land {

        terrain\_type DESERT

        land\_percent 3

        land\_position 50 50

        assign\_to\_player 1

}

### nomad\_resources

Game versions: UP/HD/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493216226&usg=AOvVaw35wsIoBHEHaRbxdmk3xr9X)

Adds the cost of a town center (275 Wood, 100 Stone) to every player's starting resources.  Use this in your custom nomad map if you want players to be able to build a town center without first gathering wood.

* In DE, this adds the actual cost of a town center for the player's civilization.  ie. Incas only get an extra 85 stone.

Example:

<PLAYER\_SETUP>

nomad\_resources

### force\_nomad\_treaty

Game versions: DE only

Activates a treaty period on nomad maps which lasts until every player has completed a town center or until 5 min have elapsed, whichever occurs first.  Nomad treaty prevents combat and prevents construction within 10 tiles of another player's town center (foundation).

* The border of the 10 tile radius is visible in explored tiles, which makes finding enemy town centers much easier.  For this reason, nomad maps for tournament games often intentionally choose not to have a nomad treaty, while instead having rules against early villager fighting.

Example:

<PLAYER\_SETUP>

nomad\_resources

force\_nomad\_treaty

### behavior\_version  VersionNumber

Game versions: DE only

Arguments:

* VersionNumber - number (0-2) (default: 0)

* 0 is classic behavior, and is the default
* 1 is new behavior
* (2 supposedly changes the behavior of object placement for per-player lands, but I haven't observed any noticeable differences)

Used for versioning changes that might affect how existing maps generate.  Changes land generation such that when specifying [number\_of\_tiles](#h.bzvr6x5i10na) or [land\_percent](#h.ipg3ruf70nn4), the square amount covered by the [base\_size](#h.b9qafcmyygh) is included in the total, rather than being additive.  Also fixes a bug where land order would influence the generation.

* This command can be used anywhere in your script.  Player setup seems like an appropriate place to put it, so it is listed here.
* May be used in the future to gate off more fixes and changes that might break backwards compatibility.
* To update an old map, you must increase [number\_of\_tiles](#h.bzvr6x5i10na) by (1+[base\_size](#h.b9qafcmyygh)\*2)² to get the same number of tiles as you previously had.

* You also should increase any sub-100 [land\_percent](#h.ipg3ruf70nn4) by an amount that varies with map size.

Example: Activate new land generation behavior in your script and observe that your lands get smaller.

behavior\_version 1

<LAND\_GENERATION>

create\_player\_lands {

    terrain\_type DLC\_BLACK

    number\_of\_tiles 250

    base\_size 12

}

### override\_map\_size  SideLength

Game versions: DE only

Arguments:

* SideLength - number (36-480) (default: use size set in lobby) (see: [Map Sizes](#h.qannz915qgy5))

* values smaller than 36 or larger than 480 will clamp to those limits

Used to manually adjust the square dimensions of the map.  This is used to make some of the official water maps one size larger than the size selected in the lobby.

* Only one argument is accepted, so you are still restricted to square maps.
* This command can be used anywhere in your script.  For general usage it should be used prior to any land generation, which is why it is listed here.
* Affects the scaling of elevation ([set\_scale\_by\_size](#h.8vbd2ko0sw7f) / [set\_scale\_by\_groups](#h.3vkc0lxd4r4a)), terrains ([set\_scale\_by\_size](#h.g4zvtvsbcm29) / [set\_scale\_by\_groups](#h.cl6w98j0bs9h)), and objects ([set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)).
* Can theoretically be used multiple times.  Land generation will be based on what the current size is at that point in the script.
* Does not influence the length of the wonder timer; it will only depend on the size set in the lobby.

* This can be used to reduce the wonder timer in 8 player games, by having players choose the tiny size in the lobby for a script that overrides the size to something suitable for 8 players.

Example 1: Make the map always generate at a size of 100x100 tiles.

override\_map\_size 100

Example 2: Make a map generate somewhat larger than what is set in the lobby.
if TINY\_MAP        override\_map\_size 144

elseif SMALL\_MAP        override\_map\_size 168

elseif MEDIUM\_MAP        override\_map\_size 200

elseif LARGE\_MAP        override\_map\_size 220

elseif HUGE\_MAP        override\_map\_size 240

elseif GIGANTIC\_MAP        override\_map\_size 255

endif

### set\_gaia\_civilization  CivNumber

Game versions: DE only

Arguments:

* CivNumber - number (0-43) (default: 0 - gaia) (see: [Civilizations](#h.8ctucmcvyhyv))

Set the civilization for gaia to use.  This will affect the architectural style of any gaia buildings, and the appearance of any units that have regional variations.  It will also affect any civilization bonuses, upgrades and unique technologies (relevant especially for [battle royale](#h.yaqdimuqjsaj))

* The default gaia civ in DE uses the western European architectural style.
* This command can be used anywhere in your script.  Player setup seems like an appropriate place to put it, so I have listed it here.
* If used, gaia effects (see: [Effect Constants](#h.90ed1yz7qe0h)) will no longer function when applied to units that can be player controlled.
* If used, gaia buildings with [make\_indestrucible](#h.a9ken9hkekd6) will be burning, so it is best not to use set\_gaia\_civilization if you wish to use indestructible gaia buildings.
* If used multiple times, only the final instance will apply.
* Does not work in the scenario editor.

Example: Create a Lithuanian monument for gaia somewhere on the map

set\_gaia\_civilization 35

<OBJECTS\_GENERATION>

create\_object MONUMENT

### ai\_info\_map\_type  MapType  IsNomad  IsMichi  ShowType

Game versions: All

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493226087&usg=AOvVaw34oStBE1uCyqnn_WZZJPOg)

Arguments:

* MapType - map type constant (see: [Map Types](#h.jxjsnahvu5u4)) (default: CUSTOM)

* Specify a standard map type that your map is similar to.

* IsNomad - boolean (1 or 0) (default: 0)

* Specify if your map is nomad style (no town center to start with).
* Always use this on nomad starts since it prevents issues where ally locations are revealed (fixed in DE)

* IsMichi - boolean (1 or 0) (default: 0)

* Specify if your map is Michi style (forest completely separating players).

* ShowType - boolean (1 or 0) (default: 0)

* Specify if you want your chosen map type to be shown in the objectives window (only works in UP)

Provide information about the map to AIs.  If your map is not very similar to an existing map, it is best to leave out the command entirely, or to use CUSTOM as the map type.

Example: A map that is a slightly modified version of Arabia and you want the objectives screen to say Arabia.

<PLAYER\_SETUP>

ai\_info\_map\_type ARABIA 0 0 1

### effect\_amount  EffectType  Type  AttributeType  Amount

Game versions: UP/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493228140&usg=AOvVaw0woYbTxMQTdQRBKq8Sxr-_), [UserPatch Effects Guide](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,44466,0,365&sa=D&source=editors&ust=1744981493228347&usg=AOvVaw0QngmiEJRkCYQQUrdzunGW)

Arguments:

* EffectType - effect constant (see: [Effect Constants](#h.90ed1yz7qe0h))
* Type - object/resource/technology/effect constant (see: [Objects](#h.nvxriamulybh), [Resource Constants](#h.cym0hd55425r), [Technology Constants](#h.ro59uo4jl1z3), [Miscellaneous Constants](#h.2n1q8vynhc9o), [Class Constants](#h.lvcoxxnz995p), [Advanced Genie Editor](#h.6u6ogmgec4g))
* AttributeType - attribute constant (see: [Attribute Constants](#h.oumcl095iabt))
* Amount - number

* DE only: accepts floating-point values

Modify various aspects of the gamedata, specifically for your map.  See the linked guides for a better overview of the possibilities.

* When modifying objects, you may need to target ALL hidden variations, one-by-one.
* If an object ends up with more than 32767 hitpoints, it is instantly destroyed. Be sure to consider in-game upgrades and civ bonuses.
* If you disable an object with this command, in-game techs/ages (unless disabled) may re-enable it. The civ tech tree may also override changes.
* (UP only) !C will be appended to the map name in the Objectives window.
* In vanilla UP only, the relevant constants must first be defined before use.

Example 1: Add 10000 starting food.

<PLAYER\_SETUP>

effect\_amount MOD\_RESOURCE AMOUNT\_STARTING\_FOOD ATTR\_ADD 10000

Example 2: Houses support 10/15/20/25 population in dark/feudal/castle/imperial age.

<PLAYER\_SETUP>

effect\_amount SET\_ATTRIBUTE HOUSE ATTR\_STORAGE\_VALUE 10

effect\_amount SET\_ATTRIBUTE HOUSE\_F ATTR\_STORAGE\_VALUE 15

effect\_amount SET\_ATTRIBUTE HOUSE\_C ATTR\_STORAGE\_VALUE 20

effect\_amount SET\_ATTRIBUTE HOUSE\_I ATTR\_STORAGE\_VALUE 25

Example 3: Exploding villagers.

[https://snippets.aoe2map.net/ArbalestHandCartBerserkEliteCamelArcher](https://www.google.com/url?q=https://snippets.aoe2map.net/ArbalestHandCartBerserkEliteCamelArcher&sa=D&source=editors&ust=1744981493231385&usg=AOvVaw0Q1XSBIDDDthjbIhZ4_Ew6)

Example 4: Examples from UserPatchConst file.

#const OUTLAW 158

#const RI\_LOOM 22

<PLAYER\_SETUP>

effect\_amount SET\_ATTRIBUTE VILLAGER\_CLASS ATTR\_HITPOINTS 20

effect\_percent ADD\_ATTRIBUTE VILLAGER\_CLASS ATTR\_MOVE\_SPEED 30

effect\_amount MUL\_ATTRIBUTE VILLAGER\_CLASS ATTR\_HITPOINTS 2

effect\_amount MOD\_RESOURCE AMOUNT\_STARTING\_FOOD ATTR\_ADD 20

effect\_amount MUL\_RESOURCE AMOUNT\_STARTING\_FOOD ATTR\_DISABLE 5

effect\_amount SET\_TECH\_COST RI\_LOOM AMOUNT\_GOLD 10

effect\_amount ADD\_TECH\_COST RI\_LOOM AMOUNT\_GOLD 20

effect\_amount MOD\_TECH\_TIME RI\_LOOM ATTR\_SET 60

effect\_amount ENABLE\_OBJECT TRANSPORT\_SHIP ATTR\_ENABLE 0

effect\_amount UPGRADE\_UNIT WOLF OUTLAW 0

effect\_amount DISABLE\_TECH RI\_LOOM ATTR\_DISABLE 22 /\* note that ENABLE\_TECH does not exist in DE, use MODIFY\_TECH instead \*/

effect\_amount ENABLE\_TECH RI\_LOOM ATTR\_ENABLE 22

effect\_amount MODIFY\_TECH RI\_LOOM ATTR\_SET\_TIME 60

effect\_amount SET\_PLAYER\_DATA DATA\_CIV\_NAME\_ID ATTR\_SET 10230

### effect\_percent  EffectType  Type  AttributeType  %

Game versions: UP/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493233262&usg=AOvVaw2gFpEJbJt5MOKvk77yOwBM), [UserPatch Effects Guide](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,44466,0,365&sa=D&source=editors&ust=1744981493233412&usg=AOvVaw2SzS6DT5Gsl3TibamW7ZKU)

Arguments:

* EffectType - effect constant (see: [Effect Constants](#h.90ed1yz7qe0h))
* Type - object/resource/technology/effect constant (see: [Objects](#h.nvxriamulybh), [Resource Constants](#h.cym0hd55425r), [Technology Constants](#h.ro59uo4jl1z3), [Class Constants](#h.lvcoxxnz995p), [Miscellaneous Constants](#h.2n1q8vynhc9o), [Advanced Genie Editor](#h.6u6ogmgec4g))
* AttributeType - attribute constant (see: [Attribute Constants](#h.oumcl095iabt))
* % - number

* DE only: accepts floating-point values

Same as [effect\_amount](#h.1niw1edwqhy5) but allows for greater precision.  The specified value is divided by 100 so that you can use decimal values.

Example 1: Add 0.3 speed to all villagers (30/100 = 0.3)

<PLAYER\_SETUP>

effect\_percent ADD\_ATTRIBUTE VILLAGER\_CLASS ATTR\_MOVE\_SPEED 30

Example 2: Nerf the slinging of resources by making tributing more inefficient and moving coinage to imperial age.

[https://snippets.aoe2map.net/GbetoEliteRattanArcherChemistryThalassocracy](https://www.google.com/url?q=https://snippets.aoe2map.net/GbetoEliteRattanArcherChemistryThalassocracy&sa=D&source=editors&ust=1744981493235260&usg=AOvVaw3tpNUoSosGBbpj27Kyl2mS)

### guard\_state  ObjectType  ResourceType  ResourceDelta  Flags

Game versions: UP/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493235694&usg=AOvVaw1M9vf11c-4EV6rw8zoEotc)

Arguments:

* ObjectType - object constant or class constant (see: [Objects](#h.nvxriamulybh), [Class Constants](#h.lvcoxxnz995p))

* for villagers use VILLAGER\_CLASS instead of VILLAGER

* ResourceType - resource amount constant (see: [Resource Constants](#h.cym0hd55425r))
* ResourceDelta - number (default: 0)

* DE only: accepts floating-point values

* Flags - number (0-7) (default: 0)

* 0: no flags
* 1: lose if you do not control the specified ObjectType
* 2: activate a resource trickle of the ResourceType at the level of ResourceDelta/100, as long as you control ObjectType
* 4: invert the ObjectType requirement for the other flags
* add the values to apply multiple flags

Set up additional lose conditions and/or resource trickles based on controlling or not controlling a specified object.

* Only one guard\_state command can be active in your script!
* (UP only) If used, !G will be appended to the map name in the Objectives window, along with the guard state details

Example: Activate a guardstate on the king, to make a map regicide even in other game modes.

<PLAYER\_SETUP>

guard\_state KING AMOUNT\_GOLD 0 1

Example 2: Slowly drain a player's food while they do not control the monument.

<PLAYER\_SETUP>

guard\_state MONUMENT AMOUNT\_FOOD -5 6

Example 3: Enable a small, relic-style gold trickle and configure players to be defeated if all villagers are lost.

<PLAYER\_SETUP>

guard\_state VILLAGER\_CLASS AMOUNT\_GOLD 10 3

### terrain\_state  Mode  Parameter1  Parameter2  Flags

Game versions: UP only

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493238779&usg=AOvVaw3gP4oEQMjTpCUz2beExire)

Arguments:

* Mode - number (0) (default: 0)
* Parameter1 - number (0) (default: 0)
* Parameter1 - number (0) (default: 0)
* Flags - number (0-7) (default: 0)

* 0: no flags
* 1: enable building on shallows; also allows resources to be placed on shallows
* 2: thinner blending of shallows and beach terrain
* 4: changes ice blending to use shallows-style blending
* add the values to apply multiple flags

Changes the shallows terrain to allow it to be buildable.  Can also be used to modify shallows and ice blending properties.  There may be further unknown and undocumented functionality.

* Parameters 1 and 2 are unimplemented as far as we currently know, and the only known mode is 0, so just set the first three numbers to 0 if you use this command.

Example: Activate all flags to allow for buildable shallows with alternate blending

<PLAYER\_SETUP>

terrain\_state 0 0 0 7

### weather\_type  PrecipitationStyle  LiveColor  FogColor  WaterDirection

Game versions: UP only

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493240859&usg=AOvVaw3ybXiSu7WmavyNVXoxHCCw), [Weather Effects Guide](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42296,,365&sa=D&source=editors&ust=1744981493241008&usg=AOvVaw1B7R0TJW8OqxgrNPAlz0gz)

Arguments:

* PrecipitationStyle - number (-4 to 4) (default: 0)

* 0 is no precipitation; 2 is rain; 3 is thunderstorm; 4 is snow.
* Precipitation goes west to east.  Use negative numbers for east to west.

* LiveColor - number (0 to 255) (default: 0)

* Color of terrain tinting in revealed areas.
* 0 is none; 1-255 refers to the [color palette](#h.wis031bn7kgs).

* FogColor - number (0 to 255) (default: 0)

* Color of terrain tinting in the fog of war.
* 0 is none; 1-255 refers to the [color palette](#h.wis031bn7kgs).

* WaterDirection - number (-1 to 1) (default 0)

* Direction of animated water.
* 0 is random; 1 is west to east; -1 is east to west.

Set up precipitation and terrain tinting.

* It usually looks good to match the precipitation and water direction.
* It often makes sense to pick similar colors for live and fog tinting.
* Terrain tinting looks bad on streams and recordings, so you may want to leave it out.
* In DE, consider using [color\_correction](#h.7xt01aajnkw9) instead.

Example: Westward thunderstorm

<PLAYER\_SETUP>

weather\_type -3 16 0 -1

---

##

## <LAND\_GENERATION>

Place large areas of terrain, including the player starting areas.  Required if you want to place players.  Land origins (square bases) are placed in order. After all origins are placed, all lands grow simultaneously from their origins outwards in all directions to fill the amount of space specified for each land, or until they run into a border or another land.  Land growth happens all at once!

External guide: [Land Generation in Age of Empires II](https://www.google.com/url?q=https://www.dropbox.com/scl/fi/gmk0lmwsknu8mlssgd2mb/LandStyles_explained_jan19.docx?rlkey%3Dpbizy742b6xi5vldxzfx17mkb%26dl%3D1&sa=D&source=editors&ust=1744981493243858&usg=AOvVaw03-IEambSu57p4hVQAAHT9)

### base\_terrain  TerrainType

Game versions: All

See also: [base\_terrain (elevation)](#h.y6zq54jntrkn), [base\_terrain (terrain)](#h.ptxp1ht2fh0p)

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: GRASS)
* BUG (DE): Does not default to GRASS, so make sure to specify the base terrain.

Specify a terrain to initially fill the map.  Maps with rivers going through them or oceans on the outside usually use water.  Maps with forest on the outside usually use forest terrain.

Example: Fill the map with water

<LAND\_GENERATION>

base\_terrain WATER

### base\_layer  TerrainType

Game versions: DE only

See also: [base\_layer (elevation)](#h.my6smlk88r2j), [base\_layer (terrain)](#h.nlwld8oca536)

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: no layered terrain)

Specify a terrain to layer on top of the map's [base\_terrain](#h.t4mfjnozvxwf).  This layered terrain is visual only, and does not confer any terrain properties or object restrictions.

* Must be used AFTER [base\_terrain](#h.t4mfjnozvxwf).
* If used, you must specify the same [base\_layer](#h.my6smlk88r2j) in [create\_elevation](#h.h85o0pyielaj), should you want to generate elevation on the map base terrain.

Example: Initially fill the map with dirt3, and layer snow on top of that

<LAND\_GENERATION>

base\_terrain DIRT3

base\_layer SNOW

### enable\_waves  ShowWaves

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493246832&usg=AOvVaw3WJe9yhfddTRFDxhx-hKzz)

Arguments:

* ShowWaves - boolean (1 or 0) (default: 1)

Enabled by default, so you only need to include it if you want to disable animated beach waves on your map.  Waves are only visible if the player has "Render Beach Waves" turned on in the game settings.

Example: Disable beach waves

<LAND\_GENERATION>

enable\_waves 0

### create\_player\_lands  { Attributes }

Game versions: All

Creates a land for every player.

* Usually this command is used only once, but it can be repeated to, for example, give every player two starting towns.
* Not required.  You can use [create\_land](#h.te4jg2upqvlx) with the [assign\_to\_player](#h.mok24wym6kiz) or [assign\_to](#h.b6uul7n11c6g) attributes to give lands directly to individual players instead (or in addition to creating player lands).
* If you do not give players any lands at all, you cannot give them any starting units or resources.  They will start at an entirely random location with only a town center, villagers and scout.  This is NOT recommended.
* DE: using [direct\_placement](#h.jbnjt99zhiqx) with create\_player\_lands disables the circular land positioning, so this is usually not desirable.

Example: Create player lands made of dirt

<LAND\_GENERATION>

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 20

}

### create\_land  { Attributes }

Game versions: All

Create a single non-player (neutral) land.

* Can be assigned to a player with [assign\_to\_player](#h.mok24wym6kiz) or [assign\_to](#h.b6uul7n11c6g)

Example: Create a lake in the center

<LAND\_GENERATION>

create\_land {

        terrain\_type WATER

        land\_percent 10

land\_position 50 50

}

### terrain\_type  TerrainType

Game versions: All

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: GRASS)

Specify which terrain the land should have.

Example: Create player lands made of dirt

<LAND\_GENERATION>

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 20

}

### land\_percent  %

Game versions: All

See also: [land\_percent (terrain)](#h.tzpfzbf2ze3w)

Mutually exclusive with: [number\_of\_tiles](#h.bzvr6x5i10na)

Arguments:

* % - number (0-100) (default: 100)

Percentage of the total map that the land should grow to cover.

* If land growth is constrained by borders or other lands, lands may be smaller than specified.
* For player lands ([create\_player\_lands](#h.esy5dq29i0wr)) the percentage is divided equally between all players.

Example: Allocate 20% total of the map toward player lands

<LAND\_GENERATION>

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 20

}

### number\_of\_tiles  Amount

Game versions: All

See also: [number\_of\_tiles (elevation)](#h.efs6lqjf3k0x), [number\_of\_tiles (terrain)](#h.qdz0o9mtb2hi)

Mutually exclusive with: [land\_percent](#h.ipg3ruf70nn4)

Arguments:

* Amount - number (default: [land\_percent](#h.ipg3ruf70nn4) 100)

Fixed number of tiles that the land should grow by.

* Total size of the land is number\_of\_tiles in addition to the square origin specified by [base\_size](#h.b9qafcmyygh)

* When using [behavior\_version](#h.seeuqpcozayb) 1, the square origin is included in the total number\_of\_tiles, resulting in smaller lands, unless compensated for.

* For player lands ([create\_player\_lands](#h.esy5dq29i0wr)) each player is given the specified number of tiles.

Example: Give every player 300 tiles

<LAND\_GENERATION>

create\_player\_lands {

        terrain\_type DIRT

        number\_of\_tiles 300

}

### base\_size  Radius

Game versions: All

Arguments:

* Radius - number (default: 3)

Square radius of the initially placed land origin, before any growth.

* The default of 3 results in a 7x7 land origin (49 tiles total).
* base\_size will produce a perfect square if used with [land\_percent](#h.ipg3ruf70nn4) 0 or [number\_of\_tiles](#h.bzvr6x5i10na) 0.
* base\_size is the minimum distance that a land will be placed from the edge of the map.
* Land bases are placed sequentially, so if they are large and overlap, the land placed last will be the one visible in the overlapping region.
* Non-player land bases will not overlap with each other, unless...
* If base\_size for non-player lands is too large, the land will fail to find a valid position and will be placed at the center of the map, overlapping any other lands at the center.

Example: Create a 13x13 square of ice

<LAND\_GENERATION>

create\_land {

terrain\_type ICE

base\_size 6

number\_of\_tiles 0

}

### land\_position  %X  %Y

Game versions: All

Arguments:

* %X - number (0-100) (default: random\*)

* X is the axis running from the top (southwest) to the bottom (northeast)

* %Y - number (0-99) (default: random\*)

* Y is the axis running from the left (northwest) to right (southeast)

* Note that 100 for the Y coordinate (or anything outside the map) will crash the game if your map uses [<CONNECTION\_GENERATION>](#h.urxh5ze1aaoh) and has a connection that needs to reach this land specifically, or if the land uses [assign\_to\_player](#h.mok24wym6kiz)
* \*lands without land\_position will have their randomly chosen origin in a cross-shaped area and will never be in the corners.

Specify the exact origin point for a land, as a percentage of total map dimensions.

* land\_position 50 50 is the center of the map.
* land\_position 0 0 is the west corner, 100 99 is the east corner, 100 0 is the north corner, 0 99 is the south corner.

        ![](images/image10.png)

* Ignores border restrictions
* If placed outside of specified [borders](#h.xrncn5cs75or), the land will not grow beyond its [base\_size](#h.b9qafcmyygh)
* Disabled for [create\_player\_lands](#h.esy5dq29i0wr)
* Disabled when using [assign\_to\_player](#h.mok24wym6kiz) or [assign\_to](#h.b6uul7n11c6g) for [create\_land](#h.te4jg2upqvlx), unless [direct\_placement](#h.jbnjt99zhiqx) is specified in [<PLAYER\_SETUP>](#h.1jv1nmqnml7h)
* Positions outside of the map can theoretically be used if the crash conditions are avoided.

Example: Create a lake in the center of the map

<LAND\_GENERATION>

create\_land {

terrain\_type WATER

land\_percent 10

land\_position 50 50

}

### circle\_radius  %Radius  Variance

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493258716&usg=AOvVaw2p3GbjwO8KnF_c3ZrlErY-)

Arguments:

* %Radius - number (1-50)

* It is a percentage of map width
* 0 will disable circle\_radius
* The standard radius for unconstrained lands is around 40
* Values larger than 50 will tend to force players towards the extreme edges and corners of the map

* Variance - number (default: 0)

* 0 is a perfect circle with no variance
* 20 seems to be close to the standard amount of variance when not using circle\_radius
* Very large values will tend to force players towards the corners of the map
* Each player will vary independent of the others

Used in [create\_player\_lands](#h.esy5dq29i0wr) to position the player lands in a circle with equal distance to the center, with specified variance.

* Circle radius ignores any specified [borders](#h.xrncn5cs75or) when placing the land origins, but land growth will still be constrained by borders.
* There is also a command called circle\_placement which is used in the standard maps and listed in the official documentation. That command is non-functional.
* If used for multiple unique [create\_player\_lands](#h.esy5dq29i0wr) commands, only the final radius will apply.

* BUG: if used for multiple player lands while also using [grouped\_by\_team](#h.31ppsgfv9i7y), the additional land positions will not generate properly.

* If used for [create\_land](#h.te4jg2upqvlx), it will still apply to player lands normally.
* See [Circle Radius Comparison](#h.2pk5zk5824si) in the appendix for a comparison of not using circle\_radius to a radius with no variance.

Example: Place player lands in a perfect circle close to the center of the map.

<LAND\_GENERATION>

create\_player\_lands {

terrain\_type DIRT

number\_of\_tiles 100

circle\_radius 20 0

}

### left\_border  %

### right\_border  %

### top\_border  %

### bottom\_border  %

Game versions: All

Arguments:

* % - number (0-99) (default: 0)

Specify a percentage of map width for land placement and growth to stay away from a given border.

* Left is southwest; right is northeast, top is northwest; bottom is southeast

![](images/image10.png)

* There is a hard-coded feature that makes lands look like octagons instead of squares when constrained by borders.
* Borders shift the entire circle of all the player lands
* You cannot have multiple rings of player lands with different borders; they will all be in the same circle
* Due to rounding, the exact number of tiles that a given % value corresponds to may not be the same for each side.

* For example, to stop 2 tiles from the edge on a tiny (120x120) map, a value of 2 must be used for the top and left borders, but a value of 3 is needed for the bottom and right borders.

* Negative values can be used, as long as the land origin stays inside the map.  To ensure this, do one of the following:

* Specify a [land\_position](#h.fnezpf6c85yf) within the map
* Specify a sufficiently large [base size](#h.b9qafcmyygh) (this may require manually scaling of base\_size with map size)

* BUG: asymmetric borders for player lands can cause issues when the top\_border is larger than other borders (External reference: [RMS Border Bugs Exposed](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D28,42496,0,365&sa=D&source=editors&ust=1744981493263934&usg=AOvVaw1IlsF4V1Jg2TgiT2oKnvqo)).  Avoid this by always using another border along with top\_border when creating player lands.

Example: Place all players in the top corner of the map.

<LAND\_GENERATION>

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 100

bottom\_border 60

left\_border 60

}

### border\_fuzziness  %BorderAdherence

Game versions: All

Arguments:

* %BorderAdherence - number (0-100) (default: 20)

Specifies the extent to which land growth respects [borders](#h.xrncn5cs75or) and actually stops at a border.

* Low values allow lands to exceed specified borders, giving ragged looking edges when land is constrained by borders.
* 0 causes land growth to ignore borders entirely.
* 100 (or any negative value) means that borders are fully respected, resulting in perfectly straight lands along borders.

Example: Central desert with very fuzzy borders

<LAND\_GENERATION>

create\_land {

terrain\_type DESERT

land\_position 50 50

land\_percent 100

left\_border 40

right\_border 40

top\_border 40

bottom\_border 40

border\_fuzziness 2

}

### clumping\_factor  Factor

Game versions: All

See also: [clumping\_factor (terrain)](#h.mztseaf6qfgt)

Arguments:

* Factor - number (default: 8 - different than for terrains)

* Useful range of about 0-40

The extent to which land growth prefers to clump together near existing tiles.  Moderate values (11-40) create rounder lands, while low values (0-10) create more irregular lands, and high values (40+) create lands that extend in one direction away from the origin.  Negative values create extremely snakey lands, and are generally not recommended.

Example: Create an irregularly shaped lake

<LAND\_GENERATION>

create\_land {

terrain\_type WATER

land\_percent 10

clumping\_factor 2

}

### base\_elevation  Height

Game versions: UP/HD/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493267929&usg=AOvVaw2Bl1VfpG8EsDP6g8nc5yTp)

Requires: [<ELEVATION\_GENERATION>](#h.szmawgkuqtsf) section (can be empty)

Arguments:

* Height - number (1-16) (default: 0 - not elevated)

* In UP/HD elevations higher than 7 should not be used, because objects will fail to render properly.
* In DE, elevations higher than 7 can be used, but may cause terrain rendering issues for certain screen resolutions, especially if you go higher than about 16.
* Negative values maximally elevate a land (not recommended due to rendering issues)

Elevate the entire land to the specified height.

* In HD/DE this will not work for lands with a water [terrain\_type](#h.lzceesmva36o)
* Up to a height of 9 the surrounding terrains will contain the slope, with even higher values, the remaining elevation occurs within the confines of the land.

Example: Create a palm desert land with elevation 2.

<LAND\_GENERATION>

create\_land {

        terrain\_type PALM\_DESERT

        number\_of\_tiles 128

        base\_elevation 2

}

<ELEVATION\_GENERATION>

### assign\_to\_player  PlayerNumber

Game versions: All

Mutually exclusive with: [assign\_to](#h.b6uul7n11c6g)

Arguments:

* PlayerNumber - number 1-8 (default: not assigned to any players)

Assign a land created with [create\_land](#h.te4jg2upqvlx) to one specific player, allowing you to place starting objects on that land for that player.

* Refers to lobby order -  the first person in the lobby is player 1, even if they are not blue.
* If you want to support 8 players, you must individually assign lands to all 8 players.
* Lands assigned to players who are not playing will not be created.
* All lands belonging to players will be in a circle and [land\_position](#h.fnezpf6c85yf) will be ignored, unless [direct\_placement](#h.jbnjt99zhiqx) is specified in [<PLAYER\_SETUP>](#h.1jv1nmqnml7h)
* assign\_to\_player 0 will make the land gaia's player land (not recommended!)
* negative values will create the land without assigning it to anyone.

Example: Assign a desert land to player 1

<LAND\_GENERATION>

create\_land {

        terrain\_type DESERT

        land\_percent 3

        assign\_to\_player 1

}

### assign\_to  AssignTarget  Number  Mode  Flags

Game versions: UP/DE

Mutually exclusive with: [assign\_to\_player](#h.mok24wym6kiz)

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493272196&usg=AOvVaw3JS8EIn9n38lWRB3D7TrpC)

Arguments:

* AssignTarget - [AssignTargetConstant](#h.n9ppujqraas6) (default: not assigned to any players)

* Options are AT\_PLAYER, AT\_COLOR, AT\_TEAM

* Number - varies depending on the AssignTarget

* AT\_PLAYER (1-8) - player number (refers to lobby order)
* AT\_COLOR (1-8) - player color
* AT\_TEAM (-10, -4,-3,-2,-1,0,1,2,3,4) - team number (refers to lobby order, not the number chosen by the team).  Gives the land to a player from the specified team.

* 0 is for un-teamed players
* negative values target a player NOT on the specified team
* -10 gives the land to any player
* Teams containing only 1 player do not count as teams

* Mode - number (-1, 0)

* 0 is for random selection (only matters for AT\_TEAM)
* -1 is for ordered selection (based on lobby order) (only matters for AT\_TEAM)

* Flags - number (0-3)

* 0: no flags
* 1: reset players who have already been assigned before starting
* 2: do not remember assigning this player
* 3: apply the effects of both 1 and 2

A more powerful version of [assign\_to\_player](#h.mok24wym6kiz).  Assign a land created with [create\_land](#h.te4jg2upqvlx) to one specific player, allowing you to place starting objects on that land for that player.

* If you want to support 8 players, you must individually assign lands for all players.
* Lands assigned to players who are not playing will not be created.
* All lands belonging to players will be in a circle and [land\_position](#h.fnezpf6c85yf) will be ignored, unless [direct\_placement](#h.jbnjt99zhiqx) is specified in [<PLAYER\_SETUP>](#h.1jv1nmqnml7h)
* In DE and WK the AssignTargetConstants are predefined, but in vanilla UP they must be manually defined first.

Example: Assign a new land at the map center to a random player on team 1.

<PLAYER\_SETUP>

direct\_placement

<LAND\_GENERATION>

create\_land {

        terrain\_type DIRT

        number\_of\_tiles 128

        land\_position 50 50

        assign\_to AT\_TEAM 1 0 0

}

### zone  ZoneNumber

Game versions: All

Mutually exclusive with: [set\_zone\_by\_team](#h.6pxlle5x8e8w) / [set\_zone\_randomly](#h.nweca22q5puk)

Arguments:

* ZoneNumber - number

Set a numeric zone.

Lands sharing the same zone can grow to touch each other.  If two lands have different zones, and [other\_zone\_avoidance\_distance](#h.2oebaei6j04a) is specified, land growth will avoid touching the other zone.

* Do not specify any zone if you want each player to be on their own island.
* By default lands from [create\_player\_lands](#h.esy5dq29i0wr) are each in their own unique zone (PlayerNumber - 10), while lands created with [create\_land](#h.te4jg2upqvlx) all share the same zone (-10).
* BUG (AoC/UP/HD): zone 99 will crash the game.  This bug is fixed in DE.

Example: All players are on the same continent, the rest of the map is water.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 60

zone 1

}

### set\_zone\_by\_team

Game versions: All

Mutually exclusive with: [zone](#h.li85mvsiskop) / [set\_zone\_randomly](#h.nweca22q5puk)

For [create\_player\_lands](#h.esy5dq29i0wr).  Assigns the same zone to all members of the same team.

Lands sharing the same zone can grow to touch each other.  If two lands have different zones, and [other\_zone\_avoidance\_distance](#h.2oebaei6j04a) is specified, land growth will avoid touching the other zone.

* If used with [create\_land](#h.te4jg2upqvlx), it will assign the land to the same zone as the team of player 1, even if the land is a non-player land or is the assigned land for a member of a different team.  (This is not recommended!)
* Team zones correspond to (TeamNumber - 9), so team 1 is in zone -8.

Example: Team Islands

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 80

set\_zone\_by\_team

other\_zone\_avoidance\_distance 10

left\_border 10 right\_border 10 top\_border 10 bottom\_border 10

}

### set\_zone\_randomly

Game versions: All

Mutually exclusive with: [zone](#h.li85mvsiskop) / [set\_zone\_by\_team](#h.6pxlle5x8e8w)

Lands with this attribute will randomly share zones with other lands.  Lands sharing the same zone can grow to touch each other.  If two lands have different zones, and [other\_zone\_avoidance\_distance](#h.2oebaei6j04a) is specified, land growth will avoid touching the other zone.  Specifically the land gets a random zone in the range -8 to (PlayerCount - 9).  This means:

* The land(s) will never share a zone with a land that is given a positive numeric [zone](#h.li85mvsiskop) or is a non-player land without a zone assigned.
* The land(s) may share a zone with a land that has set\_zone\_randomly or that has [set\_zone\_by\_team](#h.6pxlle5x8e8w), or that has a manually specified [zone](#h.li85mvsiskop) in the correct range.
* A non-player land with set\_zone\_randomly will never share a zone with player 1, if player 1 is using their default zone of -9.

Example: Archipelago-styled map where players might be on the same island with allies, enemies or nobody.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 80

set\_zone\_randomly

other\_zone\_avoidance\_distance 10

left\_border 10 right\_border 10 top\_border 10 bottom\_border 10

}

### other\_zone\_avoidance\_distance  Tiles

Game versions: All

Arguments:

* Tiles - number (default: 0)

Number of tiles away from a land with a different [zone](#h.li85mvsiskop) to stop land growth.  Used to create river maps and island maps.

* To keep two lands separated, both lands must have this attribute.
* When different values are used for two lands, the smaller one applies.
* This attribute also keeps randomly positioned land origins/bases the specified distance apart (regardless of zone), but can be overridden by [min\_placement\_distance](#h.6d0lk4yitd95).
* Land origins/bases may end up closer together or even touching if [land\_position](#h.fnezpf6c85yf) is specified, or if used for player lands when there are too many players crammed on too small of a map.

Example:  A rivers map where all players are separated by water, and there is a neutral island in the center.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

terrain\_type GRASS

        land\_percent 100

other\_zone\_avoidance\_distance 10

}

create\_land {

terrain\_type DIRT

land\_percent 100

land\_position 50 50

zone 1

other\_zone\_avoidance\_distance 10

}

### min\_placement\_distance  Tiles

Game versions: All

Arguments:

* Tiles - number (default: value of [other\_zone\_avoidance\_distance](#h.2oebaei6j04a) (default: 0))

Number of tiles to stay away from the origins of previously created lands when randomly selecting an origin for this land.  Previously undocumented and rarely used.

* If min\_placement\_distance is not specified, land origins will be positioned such that there is at least [other\_zone\_avoidance\_distance](#h.2oebaei6j04a) worth of space between the edges of the square origins.

* min\_placement\_distance uses the center of the origins, so for a large [base\_size](#h.b9qafcmyygh), may end up closer than an equivalent other\_zone\_avoidance\_distance.

* If too large of a value is specified and the land cannot find a valid position, it will be placed in the center, regardless of other lands already in or near the center.
* No effect when [land\_position](#h.fnezpf6c85yf) is specified.
* No effect on player lands, unless [direct\_placement](#h.jbnjt99zhiqx) is active in DE

Example: Create three deserts that have their origins at least 25 tiles from the other deserts.

<LAND\_GENERATION>

create\_land {

        terrain\_type DESERT

        land\_percent 1

min\_placement\_distance 25

}

create\_land {

        terrain\_type DESERT

        land\_percent 1

min\_placement\_distance 25

}

create\_land {

        terrain\_type DESERT

        land\_percent 1

min\_placement\_distance 25

}

### land\_id  Identifier

Game versions: All

Arguments:

* Identifier - number (default: no id)

Assign a numeric label to a land, which can later be used to place objects specifically on that land with [place\_on\_specific\_land\_id](#h.34wzlujx4lbv).  Unrelated to any zone numbers.

* Multiple lands can have the same ID.  In this case, the objects will be placed on all of them.
* Must be used after [assign\_to\_player](#h.mok24wym6kiz) / [assign\_to](#h.b6uul7n11c6g) since they will reset the ID.
* Can theoretically be used for [create\_player\_lands](#h.esy5dq29i0wr), but will disable the ability to use [set\_place\_for\_every\_player](#h.hch89ipgsvb) for object placement.  This has some application when creating "fake" player lands to generate forests or ponds between players.
* Note that objects may be placed on surrounding terrain rather than the land itself, if the surrounding terrain is something the object can be placed on.
* land\_id -9 assigns the land to be the player land of gaia (not recommended!)

Example: Create a tiny snowy island and place a gold mine on it.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 0

}

create\_land {

        terrain\_type SNOW

        land\_percent 0

land\_id 13

land\_position 50 50

}

<OBJECTS\_GENERATION>

create\_object GOLD {

place\_on\_specific\_land\_id 13

}

---

##

## <ELEVATION\_GENERATION>

Optional section used to place hills on your map.

* Elevation avoids the origins of player lands by about 9 tiles.
* If [base\_elevation](#h.ppqecxdcopxb) was specified for any lands, you must include this section, even if it is empty.
* Elevation provides a combat bonus to higher units, and a debuff to lower units.
* Hill positions are noticeably biased towards being placed in the south.  In DE, you should always use [enable\_balanced\_elevation](#h.izx21xcrwjlg) to reduce this bias.

### create\_elevation  MaxHeight  { Attributes }

Game versions: All

Arguments:

* MaxHeight - number (1-16) (default: 0 - not elevated)

Create one or more hills of random height, up to the given height.

* When creating a single hill, this hill will always attempt to reach the height specified.
* Hills with a small number of base tiles are not able to reach as high.
* HD/DE: If terrain has already been elevated with a land's [base\_elevation](#h.ppqecxdcopxb), new hills will be relative to that height.
* UP: Hills always use an absolute height, even if a terrain has already been elevated with a land's [base\_elevation](#h.ppqecxdcopxb)
* Pre-DE: maximum is 7.
* Higher elevations towards 16 may cause unwanted behavior such as TC projectiles firing in a different way.

Example: Create one hill on grassy terrain.

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain GRASS

number\_of\_tiles 600

}

### base\_terrain  TerrainType

Game versions: All

See also: [base\_terrain (land)](#h.t4mfjnozvxwf), [base\_terrain (terrain)](#h.ptxp1ht2fh0p)

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: GRASS)

Terrain on which the hill(s) should generate.  If you have multiple terrains you want hills on, then you need multiple [create\_elevation](#h.h85o0pyielaj) commands.

* Note that you only need to consider terrains from [<LAND\_GENERATION>](#h.15g4dj26anlp), as [<TERRAIN\_GENERATION>](#h.9k0loz2u36yf) occurs after elevation has already been placed.

Example: Create one hill on water terrain.

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain WATER

number\_of\_tiles 600

}

### base\_layer  TerrainType

Game versions: DE only

See also: [base\_layer (land)](#h.p6oqwj1l7flh), [base\_layer (terrain)](#h.nlwld8oca536)

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: any)

Use this attribute in addition to [base\_terrain](#h.y6zq54jntrkn) if (and only if) you specified a layer for the map base terrain at the beginning of [<LAND\_GENERATION>](#h.15g4dj26anlp).

Example: Initially fill the map with dirt3, and layer snow on top of that.  Then elevate that terrain.

<LAND\_GENERATION>

base\_terrain DIRT3

base\_layer SNOW

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain DIRT3

base\_layer SNOW

number\_of\_tiles 9320

number\_of\_clumps 20

}

### number\_of\_tiles  Amount

Game versions: All

See also: [number\_of\_tiles (land)](#h.bzvr6x5i10na), [number\_of\_tiles (terrain)](#h.qdz0o9mtb2hi)

Arguments:

* Amount - number (default: about 120 on tiny maps)

Total base tile count allocated to this [create\_elevation](#h.h85o0pyielaj) command.  If [number\_of\_clumps](#h.7u0osqxg1v3m) is specified, this value is divided equally among the clumps.

Example: Create one hill on grassy terrain.

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain GRASS

number\_of\_tiles 600

}

### number\_of\_clumps  Amount

Game versions: All

See also: [number\_of\_clumps (terrain)](#h.1tzwe1brcw80)

Arguments:

* Amount - number (default: 1)

Number of individual hills to create.  If clumps are adjacent, the hills may merge.

Example: Create 4 hills of 100 tiles each.

<ELEVATION\_GENERATION>

create\_elevation 3 {

base\_terrain GRASS

number\_of\_tiles 400

number\_of\_clumps 4

}

### set\_scale\_by\_size

Game versions: All

See also: [set\_scale\_by\_size (terrain)](#h.g4zvtvsbcm29)

Mutually exclusive with: [set\_scale\_by\_groups](#h.3vkc0lxd4r4a)

Scales [number\_of\_tiles](#h.efs6lqjf3k0x) to the map size.  Unscaled value refers to a 100x100 map (see: [Map Sizes](#h.qannz915qgy5) for the scaling table)

* BUG (AoC/UP/HD): the behavior of [set\_scale\_by\_size](#h.8vbd2ko0sw7f) and [set\_scale\_by\_groups](#h.3vkc0lxd4r4a) is inverted with each attribute scaling elevation as the other one should.  This bug is fixed in DE.
* If you see a script scaling by both size and groups, only the final attribute will apply!
* If you want to scale elevation by both groups and size, you must do so manually using [Conditionals](#h.vs551a7tyxet).

Example: Create 4 hills which become larger on larger maps.  On a small map this will be 4 clumps with a total of 400\*2.1 = 840 tiles.

<ELEVATION\_GENERATION>

create\_elevation 3 {

base\_terrain GRASS

number\_of\_tiles 400

number\_of\_clumps 4

set\_scale\_by\_size

}

### set\_scale\_by\_groups

Game versions: All

See also: [set\_scale\_by\_groups (terrain)](#h.cl6w98j0bs9h)

Mutually exclusive with: [set\_scale\_by\_size](#h.8vbd2ko0sw7f)

Scales [number\_of\_clumps](#h.7u0osqxg1v3m) to the map size.  Unscaled value refers to a 100x100 map (see: [Map Sizes](#h.qannz915qgy5) for the scaling table)

* BUG (AoC/UP/HD): the behavior of [set\_scale\_by\_size](#h.8vbd2ko0sw7f) and [set\_scale\_by\_groups](#h.3vkc0lxd4r4a) is inverted with each attribute scaling elevation as the other one should.  This bug is fixed in DE.
* If you see a script scaling by both size and groups, only the final attribute will apply!
* Unlike for terrains, for elevation this attribute does NOT increase the total tile count.
* If you want to scale elevation by both groups and size, you must do so manually using [Conditionals](#h.crt6psej7mdo).

Example: Create 400 tiles worth of hills, with the number of hills scaling to map size.  On a small map this will be 4x2.1 = 8 clumps and a total of 400 tiles.

<ELEVATION\_GENERATION>

create\_elevation 4 {

base\_terrain GRASS

number\_of\_tiles 400

number\_of\_clumps 4

set\_scale\_by\_groups

}

### spacing  Amount

Game versions: All

Arguments:

* Amount - number (1+) (default: 1 - no spacing)

Number of tiles between each elevation level.  Numbers larger than 1 will produce rings of flat terrain on each level of a hill.

Example: Create one large large hill with increased spacing.

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain GRASS

number\_of\_tiles 3000

spacing 4

}

### enable\_balanced\_elevation

Game versions: DE only

Removes the bias of hill placement towards the bottom (south) of the map.  Default is disabled, so you should always include this attribute!

* Elevation will still be slightly biased towards the south, even with this attribute.
* See [Balanced Elevation Comparison](#h.a1p1k7mg0eak) in the Appendix for a comparison with and without this attribute.

Example: Spread a large number of hills fairly across the map.  Remove enable\_balanced\_elevation to see the difference.

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain GRASS

number\_of\_tiles 9320

number\_of\_clumps 9320

enable\_balanced\_elevation

}

<TERRAIN\_GENERATION>

create\_terrain DESERT {

base\_terrain GRASS

land\_percent 100

number\_of\_clumps 9320

height\_limits 1 7

}

---

##

## <CLIFF\_GENERATION>

Optional section to include rocky impassible cliffs.

External guide: [All about Cliffs](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42261,,all&sa=D&source=editors&ust=1744981493302435&usg=AOvVaw3Sk7FZQ8vzVY1S5QWtWzv6)

* Simply typing the section header will generate default cliffs, so do not include it if you do not want cliffs!  There are no create-commands in this section.
* Cliffs avoid the origins of all lands by 22 tiles, and will not be placed on water terrains.  They also avoid any slopes.
* Cliffs create a terrain under themselves.  This is terrain 16, and looks like the normal grass.  This terrain turns into terrain 0 (GRASS) prior to [<OBJECTS\_GENERATION>](#h.unkzqmnnqr5v) but can be replaced during [<TERRAIN\_GENERATION>](#h.2mwmqwe7m0vw)
* Cliffs provide a combat bonus to units shooting from the top of a cliff.

### cliff\_type  CliffType

Game versions: DE only

Arguments:

* CliffType - cliff type constant (see: [Cliff Types](#h.uow2rvrpkup5)) (default: gray granite cliffs)

Choose the color of the cliffs to match the theme of your map.

Currently the following are available:

* CT\_GRANITE
* CT\_DESERT
* CT\_SNOW
* CT\_MARBLE
* CT\_LIMESTONE

Example: Make the cliffs brown to match dirt and desert terrains:

<CLIFF\_GENERATION>

cliff\_type CT\_DESERT

### min\_number\_of\_cliffs  Amount

### max\_number\_of\_cliffs  Amount

Game versions: All

Arguments:

* Amount - number (default: min 3, max 8)

* Make sure min does not exceed max.

Set the minimum and maximum number of distinct cliffs to create.  The actual number of cliffs is chosen at random from between min (inclusive) and max (exclusive).  Does not scale with [map size](#h.qannz915qgy5), so you must do so manually using [Conditionals](#h.vs551a7tyxet).

Example: Create 5-7 cliffs on your map.

<CLIFF\_GENERATION>

min\_number\_of\_cliffs 5

max\_number\_of\_cliffs 8

### min\_length\_of\_cliff  Length

### max\_length\_of\_cliff  Length

Game versions: All

Arguments:

* Length - number (3+) (default: min 5, max 9)

* Make sure min does not exceed max, otherwise the game will crash.

Cliff lengths are chosen at random from between min and max (inclusive).  The unit is NOT tiles, but rather "cliff segments".

* Length 3 is 12 tiles, 4 is 15 tiles, 5 is 18 tiles, etc.
* Minimum must be at least 3 for cliffs to appear at all.
* Cliffs may end up shorter than expected if they run out of space.

Example: Create exactly 10 cliffs with lengths 12-18 tiles

<CLIFF\_GENERATION>

min\_number\_of\_cliffs 10

max\_number\_of\_cliffs 10

min\_length\_of\_cliff 3

max\_length\_of\_cliff 5

### cliff\_curliness  %

Game versions: All

Arguments:

* % - number (0-100) (default: 36)

The chance that a cliff changes direction at each segment.  Use low values for straight cliffs and high values for curly cliffs.

Example: Create cliffs that are more curly than usual.

<CLIFF\_GENERATION>

min\_number\_of\_cliffs 10

max\_number\_of\_cliffs 10

min\_length\_of\_cliff 10

max\_length\_of\_cliff 10

cliff\_curliness 50

### min\_distance\_cliffs  Distance

Game versions: All

Arguments:

* Distance - number (default: 2)

Minimum distance in "cliff units" between separate cliffs.

* 0 is 0 tiles, 1 is 3 tiles, 2 is 6 tiles, etc.

Example: Fill the map with cliffs that stay only 3 tiles from other cliffs.

<CLIFF\_GENERATION>

min\_number\_of\_cliffs 9999

max\_number\_of\_cliffs 9999

min\_distance\_cliffs 1

### min\_terrain\_distance  Distance

Game versions: All

Arguments:

* Distance - number (default: 2)

Minimum distance in "cliff units" that cliffs will avoid water terrains by.

* 0 is 0 tiles, 1 is 3 tiles, 2 is 6 tiles, etc.
* Note that this only considers terrains from [<LAND\_GENERATION>](#h.15g4dj26anlp), as [<TERRAIN\_GENERATION>](#h.2mwmqwe7m0vw) occurs after cliffs have already been placed.

Example: Fill the map with cliffs that stay only 3 tiles from water and 0 tiles from each other.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

terrain\_type GRASS

        land\_percent 100

other\_zone\_avoidance\_distance 10

}

<CLIFF\_GENERATION>

min\_number\_of\_cliffs 9999

max\_number\_of\_cliffs 9999

min\_distance\_cliffs 0

min\_terrain\_distance 1

---

##

## <TERRAIN\_GENERATION>

Replace terrains with other terrains.  Often used to place clumps of forest and to make the map look nice by mixing terrains for visual diversity.  Terrain generation occurs after lands, elevation and cliffs, but before connections.  Terrains are generated sequentially in the order they appear in the script.  Terrain positions cannot be directly specified.

### color\_correction  ColorCorrectionType

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493310945&usg=AOvVaw3sZJscOPXJmhGpcHZfyzlc)

Arguments:

* ColorCorrectionType - color correction constant (see: [Season Types](#h.ptggu3c4a8jy)) (default: no color correction)

Specify a color correction type to apply on your map.  Controlled by the "Map Lighting" setting in-game.

* on UP, use [weather\_type](#h.ht15fzasksgc) instead.

Example: Desert-themed lighting

<TERRAIN\_GENERATION>

color\_correction CC\_DESERT

### create\_terrain  TerrainType  { Attributes }

Game versions: All

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: GRASS)

Create a clump of terrain.  The exact behavior is dependent on the attributes specified.

Example: Create a large clump of forest terrain on grass terrain

<TERRAIN\_GENERATION>

create\_terrain FOREST {

base\_terrain GRASS

land\_percent 10

}

### base\_terrain  TerrainType

Game versions: All

See also: [base\_terrain (land)](#h.t4mfjnozvxwf), [base\_terrain (elevation)](#h.y6zq54jntrkn)

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: GRASS)

Specify the base terrain on which you want to place your new terrain.

* BUG (DE): Does not default to GRASS, so make sure to specify the base terrain.

Example: Create a large clump of forest terrain on grass terrain, then create water on the forest

<TERRAIN\_GENERATION>

create\_terrain FOREST {

base\_terrain GRASS

land\_percent 10

}

create\_terrain WATER {

    base\_terrain FOREST

}

### base\_layer  TerrainType

Game versions: DE only

See also: [base\_layer (land)](#h.p6oqwj1l7flh), [base\_layer (elevation)](#h.my6smlk88r2j),

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: none)

Specify a layered terrain on which you want to place your new terrain.

* If used together with [base\_terrain](#h.ptxp1ht2fh0p), the new terrain will be placed only where both the base and the layer apply.

Example: Layer desert on grass, and then place water on the layered desert.

<TERRAIN\_GENERATION>

create\_terrain DESERT {

base\_terrain GRASS

land\_percent 10

terrain\_mask 1

}

create\_terrain WATER {

base\_layer DESERT

}

### beach\_terrain  TerrainType

Game versions: DE only

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: BEACH)

Specify a terrain that should be placed where the current terrain borders water.

* If a non-beach terrain is specified, players will not be able to build docks on this coastline
* If a water terrain is specified, it will fully replace the terrain specified in [create\_terrain](#h.acnibljecbfg), so this is NOT recommended.
* BUG: beach\_terrain does not work when a <CONNECTION\_GENERATION> section is present

Example: Create a dirt island with beaches that have vegetation.

<LAND\_GENERATION>

base\_terrain WATER

<TERRAIN\_GENERATION>

create\_terrain DIRT {

number\_of\_tiles 500

spacing\_to\_other\_terrain\_types

base\_terrain WATER

beach\_terrain DLC\_BEACH2

}

### terrain\_mask  Layer

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493317363&usg=AOvVaw1C6HyfqirbqjhqC1_0btZz)

Arguments:

* Layer - number (1,2) (default: 0 - no masking)

* 1 - new terrain is masked over the base terrain and inherits its properties
* 2 - new terrain is masked under the base terrain and provides new properties

Enables terrain masking/layering for the terrain being created.  Terrain inherits all properties, placement restrictions, automatic objects (such as trees for forest terrains), minimap color, etc. from the terrain underneath (ie. [base\_terrain](#h.ptxp1ht2fh0p) when masking over, or [create\_terrain](#h.acnibljecbfg) when masking under)

* Terrain masking is a great way to blend terrains in a realistic and visually appealing manner.
* Masking layers 1 and 2 have different visual masking patterns.
* Terrain will have animated water if ANY of the component terrains are water.
* Legacy terrains that are already a blend of two texture files cannot be visually masked.  They will contribute fully to the appearance of the final terrain.  These terrains are:

* GRASS\_SNOW, DIRT\_SNOW, [dirt snow foundation], DLC\_MOORLAND, DLC\_JUNGLELEAVES, [road snow], [road fungus], DLC\_DRYROAD, DLC\_JUNGLEROAD, DLC\_ROADGRAVEL

* There are also some special cases with beach terrains, which may not always mask as expected.  (potentially a bug)

Example: Snow is masked on top of grass.  Will produce grass decoration objects.

<TERRAIN\_GENERATION>

create\_terrain SNOW

{

  base\_terrain GRASS

  land\_percent 50

  terrain\_mask 1

}

Example2: Snow is masked underneath grass.  Would produce snow decoration objects, if there were any in the game.

<TERRAIN\_GENERATION>

create\_terrain SNOW {

base\_terrain GRASS

land\_percent 50

terrain\_mask 2

}

### spacing\_to\_other\_terrain\_types  Distance

Game versions: All

Arguments:

* Distance - number (default: 0)

Minimum distance that this terrain will stay away from other terrain types.

* Only considers existing terrains at the time of generation - terrains generated later will need their own spacing.
* Terrains will not stay away from the same terrain type created previously.  This requires the use of an intermediate placeholder terrain.
* Also affects the distance that the terrain will stay away from cliffs (because cliffs generate their own terrain underneath them - terrain 16)
* When used with [set\_flat\_terrain\_only](#h.4300mvgw1xz7) it also affects the distance that the terrain will stay away from slopes.

Example: Create a lake, and then fill the rest of the map with a forest which stays 10 tiles away from the water.

<TERRAIN\_GENERATION>

create\_terrain WATER {

base\_terrain GRASS

land\_percent 10

}

create\_terrain FOREST {

base\_terrain GRASS

spacing\_to\_other\_terrain\_types 10

land\_percent 100

}

### set\_flat\_terrain\_only

Game versions: All

Requires: [spacing\_to\_other terrain\_types](#h.dzdzen1yp2wx) > 0

The terrain will avoid sloped tiles by the distance specified in [spacing\_to\_other\_terrain\_types](#h.dzdzen1yp2wx)

* Only works when a distance of at least 1 has been specified.

Example: Create a hill where the bottom and top are desert, but the slope is grass

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain GRASS

number\_of\_tiles 3000

number\_of\_clumps 1

}

<TERRAIN\_GENERATION>

create\_terrain DESERT {

base\_terrain GRASS

land\_percent 100

number\_of\_clumps 9320

spacing\_to\_other\_terrain\_types 1

set\_flat\_terrain\_only

}

### land\_percent  %

Game versions: All

See also: [land\_percent (land)](#h.ipg3ruf70nn4),

Mutually exclusive with: [number\_of\_tiles](#h.qdz0o9mtb2hi)

Arguments:

* % - number (1-100) (default: [number\_of\_tiles](#h.qdz0o9mtb2hi))

Percentage of the total map allocated to this [create\_terrain](#h.acnibljecbfg) command.  If [number\_of\_clumps](#h.1tzwe1brcw80) is specified, this value is divided equally among the clumps.

* Terrain will only be replaced where the appropriate [base\_terrain](#h.ptxp1ht2fh0p) or [base\_layer](#h.nlwld8oca536) is present, and will only replace the specified number of individual clumps, so it will not necessarily fill 100% of the map if set to 100.

Example: Create a desert that covers 50% of the map

<TERRAIN\_GENERATION>

create\_terrain DESERT {

base\_terrain GRASS

land\_percent 50

}

### number\_of\_tiles  Amount

Game versions: All

See also: [number\_of\_tiles (land)](#h.bzvr6x5i10na),  [number\_of\_tiles (elevation)](#h.efs6lqjf3k0x)

Mutually exclusive with: [land\_percent](#h.tzpfzbf2ze3w)

Arguments:

* Amount - number (default:122 tiles on a tiny map)

Total tile count allocated to this [create\_terrain](#h.acnibljecbfg) command.  If [number\_of\_clumps](#h.7u0osqxg1v3m) is specified, this value is divided equally among the clumps.

Example: Create a 500-tile lake

<TERRAIN\_GENERATION>

create\_terrain WATER {

base\_terrain GRASS

number\_of\_tiles 500

set\_avoid\_player\_start\_areas

}

### number\_of\_clumps  Amount

Game versions: All

See also: [number\_of\_clumps (terrain)](#h.1tzwe1brcw80)

Arguments:

* Amount - number (default: 1)

* A maximum of 9320 should be used when also specifying [s](#h.cl6w98j0bs9h)[et\_scale\_by\_groups](#h.cl6w98j0bs9h)

Number of individual terrain patches to create.

* If clumps are larger than expected (or total count is lower than expected), several adjacent clumps have merged.

Example: Create 40 forest clumps on grass terrain.

<TERRAIN\_GENERATION>

create\_terrain FOREST {

base\_terrain GRASS

land\_percent 20

number\_of\_clumps 40

}

### clumping\_factor  Factor

Game versions: All

See also: [clumping\_factor (land)](#h.7e3knrokkcni)

Arguments:

* Factor - number (default: 20 - different than for lands)

* Useful range of about 0 - 25

The extent to which terrain tiles prefer to be together next to other tiles of the same clump.  Moderate values (5-25) create rounder terrain patches, while low values (0-5) create more irregular terrain patches.  Negative values create extremely snakey terrains.

Example: Create a regularly-shaped bamboo forest

<TERRAIN\_GENERATION>

create\_terrain BAMBOO {

base\_terrain GRASS

number\_of\_tiles 500

clumping\_factor 20

}

### set\_scale\_by\_size

Game versions: All

See also: [set\_scale\_by\_size (elevation)](#h.8vbd2ko0sw7f)

Mutually exclusive with: [set\_scale\_by\_groups](#h.cl6w98j0bs9h)

Scales [number\_of\_tiles](#h.qdz0o9mtb2hi) to the map size.  Unscaled value refers to a 100x100 map (see: [Map Sizes](#h.qannz915qgy5) for the scaling table)

* If you see a script scaling by both size and groups, only the final attribute will apply!
* If you want to scale by both groups and size, use [set\_scale\_by\_groups](#h.cl6w98j0bs9h) instead.

Example: Create 4 lakes which become larger on larger maps.  On a small map this will be 4 clumps with a total of 400\*2.1 = 840 tiles.

<TERRAIN\_GENERATION>

create\_terrain WATER {

base\_terrain GRASS

number\_of\_clumps 4

number\_of\_tiles 400

set\_scale\_by\_size

}

### set\_scale\_by\_groups

Game versions: All

See also: [set\_scale\_by\_groups (elevation)](#h.3vkc0lxd4r4a)

Mutually exclusive with: [set\_scale\_by\_size](#h.g4zvtvsbcm29)

Scales [number\_of\_clumps](#h.1tzwe1brcw80) to the map size.  Unscaled value refers to a 100x100 map (see: [Map Sizes](#h.qannz915qgy5) for the scaling table)

* If you see a script scaling by both size and groups, only the final attribute will apply!
* When used with [number\_of\_tiles](#h.efs6lqjf3k0x), the total tiles are also scaled to map size as well (but only for terrains, not for elevation).

Example: Create 400 tiles worth of lakes, with the number of lakes AND the total number of tiles scaling to map size.  On a small map this will be 4x2.1 = 8 clumps with a total of 400\*2.1 = 840 tiles.

<TERRAIN\_GENERATION>

create\_terrain WATER {

base\_terrain GRASS

number\_of\_clumps 4

number\_of\_tiles 400

set\_scale\_by\_groups

}

### set\_avoid\_player\_start\_areas  Distance

Game versions: All

Arguments:

* Distance - number (default: 0 - no avoidance)

* Defaults to 13, if you specify the argument but omit the distance.
* This argument can ONLY be specified in DE

The terrain will avoid the origins of player lands by the specified number of tiles (with some variance).

* Useful to prevent forests or water terrain from being directly under the town center.
* In DE the distance can be adjusted.

Example: Forest Nothing with small clearings

<TERRAIN\_GENERATION>

create\_terrain FOREST {

base\_terrain GRASS

land\_percent 100

number\_of\_clumps 999

set\_avoid\_player\_start\_areas 12

}

### height\_limits  Min  Max

Game versions: All

Arguments:

* Min - number (default: none)
* Max - number (default: none)

The terrain will only be placed on tiles of height between min and max (inclusive).

* For most purposes, values between 0-7 are useful.  0 being the standard non-elevated height and 7 being the max height that can be produced by [create\_elevation](#h.h85o0pyielaj)

Example: Create a hill and place desert terrain only on the slopes

<ELEVATION\_GENERATION>

create\_elevation 7 {

base\_terrain GRASS

number\_of\_tiles 3000

number\_of\_clumps 1

}

<TERRAIN\_GENERATION>

create\_terrain DESERT {

base\_terrain GRASS

land\_percent 100

number\_of\_clumps 9320

height\_limits 1 6

}

---

##

## <CONNECTION\_GENERATION>

Optional section to replace terrains with other terrains, specifically along a path between the origins of lands.  Can be used to create roads between players, shallows across rivers, and to ensure that forests do not completely separate players.

* You can only specify whole systems of connections, not individual connections.
* Connections are processed in order.
* If the connection between two locations is not possible, that connection will not be produced at all.

### accumulate\_connections

Game versions: DE only

Can be used to revert a DE-specific behavior change where all connections are based on the terrain prior to connection generation, and replacing terrain created by earlier connections is impossible.

* Using this allows you to replace terrains created in previous connections.

Example: Create a wide gap through a forest and then run a road through the created gap.

<LAND\_GENERATION>

base\_terrain FOREST

create\_player\_lands {

terrain\_type FOREST

other\_zone\_avoidance\_distance 10

}

<CONNECTION\_GENERATION>

accumulate\_connections

create\_connect\_all\_lands {

replace\_terrain FOREST LEAVES

terrain\_size FOREST 10 0

}

create\_connect\_all\_lands {

replace\_terrain LEAVES ROAD

terrain\_size LEAVES 1 0

}

### create\_connect\_all\_players\_land  { Attributes }

Game versions: All

Connections will be generated between the origins of all player lands, and all lands assigned to players.

* Connections may still pass through neutral lands if the cost is favorable.

Example: connect all players with dirt terrain

<LAND\_GENERATION>

create\_player\_lands {

terrain\_type DESERT

number\_of\_tiles 100

}

<CONNECTION\_GENERATION>

create\_connect\_all\_players\_land {

default\_terrain\_replacement DIRT

}

### create\_connect\_teams\_lands  { Attributes }

Game versions: All

Connections will be generated between the origins of player lands belonging to members of the same team.

* Connections may still pass through neutral or enemy lands if the cost is favorable.
* By default, players are on their own team in the scenario editor, so keep this in mind when testing in the scenario editor.

* You can use the diplomacy tab to simulate team setups.

Example: connect team members with a road

<LAND\_GENERATION>

create\_player\_lands {

terrain\_type DESERT

number\_of\_tiles 100

}

<CONNECTION\_GENERATION>

create\_connect\_teams\_lands {

replace\_terrain FOREST ROAD

replace\_terrain GRASS ROAD

}

### create\_connect\_all\_lands  { Attributes }

Game versions: All

Connections will be generated between the origins of all lands.

Example: interconnect all player islands and neutral islands.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

terrain\_type DESERT

number\_of\_tiles 100

}

create\_land {

terrain\_type FOREST

number\_of\_tiles 100

land\_position 99 1

}

create\_land {

terrain\_type PINE\_FOREST

number\_of\_tiles 100

land\_position 50 50

}

<CONNECTION\_GENERATION>

create\_connect\_all\_lands {

replace\_terrain WATER SHALLOW

}

### create\_connect\_same\_land\_zones  { Attributes }

Game versions: All

Behaves identically to [create\_connect\_all\_lands](#h.wm3xy9f5nbd9)

* Previously undocumented, and therefore not typically used.

Example: see [create\_connect\_all\_lands](#h.wm3xy9f5nbd9)

### create\_connect\_to\_nonplayer\_land  { Attributes }

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493342125&usg=AOvVaw0rPxBz181zr36I-h0geOBN)

Connect all player lands to all neutral lands, but do not directly generate connections between individual players.

* BUG: create\_connect\_to\_nonplayer\_land blocks all future connection generation
* BUG: It also blocks all team connection generation (except those involving player 1), when used after [create\_connect\_teams\_lands](#h.sbxghl4uf1bm)

Example: connect players to a central desert, but not directly to each other

<LAND\_GENERATION>

create\_player\_lands {

terrain\_type DIRT2

number\_of\_tiles 100

}

create\_land {

terrain\_type DESERT

number\_of\_tiles 500

land\_position 50 50

}

<CONNECTION\_GENERATION>

create\_connect\_to\_nonplayer\_land {

replace\_terrain GRASS ROAD2

}

### default\_terrain\_replacement  TerrainType

Game versions: All

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk))

Replace ALL terrain in the connection with the specified terrain.

* Useful for debugging purposes to quickly visualize all connection paths.
* Overrides any previously specified [replace\_terrain](#h.5h9ggnuativl) attributes, so for best results, it should be used before any such attributes.

Example: Replace all connecting terrain with road, but replace water with shallows instead.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

land\_percent 100

other\_zone\_avoidance\_distance 10

}

<CONNECTION\_GENERATION>

create\_connect\_all\_players\_land {

default\_terrain\_replacement ROAD

replace\_terrain WATER SHALLOW

}

Example 2: Replace everything with ice to see which routes the connections are taking.

<CONNECTION\_GENERATION>

create\_connect\_all\_lands {

default\_terrain\_replacement ICE

}

### replace\_terrain  TerrainTypeOld  TerrainTypeNew

Game versions: All

Arguments:

* TerrainTypeOld - terrain constant (see: [Terrains](#h.3bdjnf7tryyk))
* TerrainTypeNew - terrain constant (see: [Terrains](#h.3bdjnf7tryyk))

If the specified terrain is part of the connection, replace it with the new terrain specified.

* This attribute can, and should, be used multiple times for different terrains.
* A terrain can be replaced with itself.
* Connections can pass through terrains even if they are not specified.
* DE: The old terrain refers to the terrain that was present at the beginning of [<CONNECTION\_GENERATION>](#h.urxh5ze1aaoh) - even if that terrain has already been replaced by a previous command or attribute.  This behavior can be disabled by using [accumulate\_connections](#h.bd2l5930vfzf)

Example: replace several terrains in a connection

<CONNECTION\_GENERATION>

create\_connect\_all\_players\_land {

replace\_terrain GRASS DIRT2

replace\_terrain FOREST LEAVES

replace\_terrain SNOW\_FOREST GRASS\_SNOW

replace\_terrain DIRT DIRT3

replace\_terrain WATER SHALLOW

}

### terrain\_cost  TerrainType  Cost

Game versions: All

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk))
* Cost - number (0-4294967296) (default 1)

* 0 (or any negative value) means that the connection CANNOT pass through the specified terrain at all, so 1 is the "lowest" cost
* For most usual applications a cost range of 1-15 is sufficient
* DE only: accepts floating-point values

The cost of having the connection run through the specified terrain.

* This attribute can be used multiple times for different terrains.

* If all costs are equal, the connections will be straight lines.
* If some costs are higher, the algorithm will prefer going though lower cost routes, even if they are longer than the more direct route.
* A cost of 0 will prevent the connection generation from running through that terrain.  If a land origin is on such a terrain, or such a terrain MUST be crossed, then the connections to that land will not be generated at all.  This can be used to manipulate connections to only connect certain lands and not others.

* Doing this excessively can slow down the map generation time.

Example: generate connections that prefer going through grass and generally avoid forests and deeper water

<CONNECTION\_GENERATION>

create\_connect\_all\_players\_land {

replace\_terrain GRASS ROAD

replace\_terrain FOREST LEAVES

replace\_terrain WATER SHALLOW

replace\_terrain MED\_WATER SHALLOW

replace\_terrain DEEP\_WATER SHALLOW

terrain\_cost GRASS 1

terrain\_cost FOREST 7

terrain\_cost WATER 7

terrain\_cost MED\_WATER 12

terrain\_cost DEEP\_WATER 15

}

### terrain\_size  TerrainType  Radius  Variance

Game versions: All

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk))
* Radius - number (default: 1)

* Given that a Ludicrously-sized map is 480 tiles wide, 961 would be enough to cover the entire map in all situations.

* Variance - number (default: 0)

When a connection passes through a tile of the specified terrain, the area within radius +/- variance will be subject to [replace\_terrain](#h.5h9ggnuativl) / [default\_terrain\_replacement](#h.p16vd5cszmhm) and terrains will be replaced accordingly.

* This attribute can be used multiple times for different terrains.

* A radius of 0 will still replace a single-tile width path.
* Variance is randomly selected for each tile crossed.
* If variance is larger than radius, it can reduce the radius to a negative value, in which case no terrain will be replaced around these specific locations.

Example: Connect players with a variable ragged-looking road, and with shallows that are slightly wider.

<CONNECTION\_GENERATION>

create\_connect\_all\_players\_land {

replace\_terrain GRASS ROAD

replace\_terrain WATER SHALLOW

terrain\_size GRASS 1 1

terrain\_size WATER 3 1

}

---

##

## <OBJECTS\_GENERATION>

Place buildings, units, resources, animals, straggler trees, decoration, etc.  Objects are placed in order.  Normally, only 1 object can be placed per tile.  If an object cannot find a valid position, it will not generate at all.  So you should place the most important objects first.  There are a few unusual cases:

* Creating the object VILLAGER without specifying the amount will give each civilization their correct number of starting villagers.

* In DE this has changed and everyone gets 3 villagers to start, with the extra ones being spawned by the town center (to prevent Chinese from being too strong on nomad starts).

* The object SCOUT will give an eagle to mesoamerican civilizations and a scout to all other civilizations.
* Walls have some special behavior (see: [Walls](#h.q7o6xdvi0noo))

### create\_actor\_area  X  Y  Identifier  Radius

Game versions: DE only

See also: [actor\_area](#h.obv5ypy66a57)

Arguments:

* X - number (x-coordinate in tiles; see [Map Sizes](#h.qannz915qgy5))
* Y - number (y-coordinate in tiles; see [Map Sizes](#h.qannz915qgy5))
* Identifier - number
* Radius - number (square radius in tiles)

Create an [actor area](#h.obv5ypy66a57) at the given location (rather than being associated with a specific object), with the ID and radius specified.

* These actor areas are created before any [create\_object](#h.2vz7nxt2afqo) commands are handled, regardless of their position in the script.
* Useful for making certain objects avoid certain positions or areas of the map
* You can also specify coordinates outside of the map, which can be useful with a sufficiently large radius to avoid the map edges
* Note that the X and Y coordinates are in tiles, NOT % of map width.  They must be manually scaled to map size.  See [Map Sizes](#h.qannz915qgy5) for the side length on each map size.
* Multiple actor areas can share the same identifier.
* create\_actor\_area will crash the game if no lands are generated on the map.  This should not be an issue on completed maps, since you always have lands.

Example: Create an actor area that prevents relics from spawning near the center of the map

<OBJECTS\_GENERATION>

if TINY\_MAP    create\_actor\_area 60 60 1234 30

elseif SMALL\_MAP create\_actor\_area 72 72 1234 36

elseif MEDIUM\_MAP create\_actor\_area 84 84 1234 42

elseif LARGE\_MAP create\_actor\_area 100 100 1234 50

elseif HUGE\_MAP create\_actor\_area 110 110 1234 55

elseif GIGANTIC\_MAP create\_actor\_area 120 120 1234 60

elseif LUDIKRIS\_MAP create\_actor\_area 240 240 1234 120

endif

create\_object RELIC {

    number\_of\_objects 500

    set\_gaia\_object\_only

    avoid\_actor\_area 1234

}

### create\_object  ObjectType  { Attributes }

Game versions: All

Arguments:

* ObjectType - object constant (see: [Objects](#h.nvxriamulybh))

Place the specified object, according to the chosen attributes.

Example: Give all players a town center.

<OBJECTS\_GENERATION>

create\_object TOWN\_CENTER {

set\_place\_for\_every\_player

max\_distance\_to\_players 0

}

### number\_of\_objects  Amount

Game versions: All

Arguments:

* Amount - number (default: 1)

* A maximum of 9320 should be used when also specifying [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)

Number of objects to create.

Example: Place 10 individual gold mines on the map.

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_objects 10

}

### number\_of\_groups  Amount

Game versions: All

Arguments:

* Amount - number (default: individual objects - no groups)

* A maximum of 9320 should be used when also specifying [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)

Place the specified number of groups, which each consist of the number of individual objects chosen in [number\_of\_objects](#h.btcx5h61er65)

* Total objects = [number\_of\_objects](#h.btcx5h61er65) x number\_of\_groups

Example: Place 20 groups of each 5 boars.

<OBJECTS\_GENERATION>

create\_object BOAR {

number\_of\_objects 5

number\_of\_groups 20

}

### group\_variance  Amount

Game versions: All

Arguments:

* Amount - number (default: 0)

The [number\_of\_objects](#h.btcx5h61er65) is randomly varied by up to the amount specified, with maximum variance in the positive direction being reduced by 1.

* A minimum of 1 object will always be generated, even if the variance would make the count 0 or negative.
* Note that each group varies independently, so this is not suitable for ensuring fair player starting resources.  Consider using [Random Code](#h.87mv66lnefdm) for such cases.

Example: Create 10 patches with each 2-7 forage bushes.

<OBJECTS\_GENERATION>

create\_object FORAGE {

    number\_of\_objects 5

    number\_of\_groups 10

    group\_variance 3

    set\_tight\_grouping

}

### group\_placement\_radius  Radius

Game versions: All

Arguments:

* Radius - number (default: 3 = a 7x7 area)

Specify the number of tiles out from the central tile that objects belonging to the same group may spawn.

* Activates grouping behavior.

* Useful for keeping gold/stone/berries from forming long lines.
* If the [number\_of\_objects](#h.btcx5h61er65) exceeds the available number of tiles, then a perfect square worth of objects will be filled.
* If used with a group of objects that have [set\_loose\_grouping](#h.umboa0q57v9y) and [set\_circular\_placement](#h.15fez3e52vqr), the area will be a circle instead of a square.

Example: Give each player forage bushes that must stay in a 3x3 area.

<OBJECTS\_GENERATION>

create\_object FORAGE {

number\_of\_objects 7

set\_tight\_grouping

group\_placement\_radius 1

set\_gaia\_object\_only

set\_place\_for\_every\_player

min\_distance\_to\_players 7

max\_distance\_to\_players 8

}

### set\_tight\_grouping

Game versions: All

Mutually exclusive with: [set\_loose\_grouping](#h.umboa0q57v9y)

Objects belonging to the same group must be in adjacent tiles.  Commonly used for berries, gold and stone.

* Activates grouping behavior.
* Objects that are larger than one tile and cannot overlap (most buildings), will not be placed when using tight grouping.
* NOTE: most constraints on object placement (ex. [avoid\_forest\_zone](#h.ym7v1j9vbnle), [min\_distance\_to\_map\_edge](#h.w2q69orjs3l3), [min\_distance\_group\_placement](#h.b2u5jna014lf), [avoid\_actor\_area](#h.cgoa0e8x398u)) apply only to the center of the group, not the individual group members.  Use [set\_loose\_grouping](#h.umboa0q57v9y) if you want constraints to apply to group members individually.

Example: Far player stone.

<OBJECTS\_GENERATION>

create\_object STONE {

number\_of\_objects 4

group\_placement\_radius 2

set\_tight\_grouping

set\_gaia\_object\_only

set\_place\_for\_every\_player

min\_distance\_to\_players 20

max\_distance\_to\_players 27

}

### set\_loose\_grouping

Game versions: All

Mutually exclusive with: [set\_tight\_grouping](#h.ksq6iglmnili)

Objects belonging to the same group can be placed anywhere within the confines of [group\_placement\_radius](#h.675xoyq748tw)

* Activates grouping behavior.

* Loose grouping is the default type of grouping, so you can omit this attribute if you specify [group\_placement\_radius](#h.675xoyq748tw)
* Commonly used for sheep and deer.
* When used with [set\_circular\_placement](#h.15fez3e52vqr), the [group\_placement\_radius](#h.675xoyq748tw) becomes round.
* NOTE: most constraints on object placement (ex. [avoid\_forest\_zone](#h.ym7v1j9vbnle), [min\_distance\_to\_map\_edge](#h.w2q69orjs3l3), [min\_distance\_group\_placement](#h.b2u5jna014lf), [avoid\_actor\_area](#h.cgoa0e8x398u)) apply to each group member individually.  However, the game doesn't check if there is enough room for the whole group to spawn when choosing a location for the group, so this can cause issues where some group members fail to spawn.  For important objects with many constraints on placement, consider using [set\_tight\_grouping](#h.ksq6iglmnili) instead.

Example: Give players a group of 7 deer.

<OBJECTS\_GENERATION>

create\_object DEER {

number\_of\_objects 7

number\_of\_groups 1

group\_placement\_radius 5

set\_loose\_grouping

set\_gaia\_object\_only

set\_place\_for\_every\_player

min\_distance\_to\_players 14

max\_distance\_to\_players 22

}

### min\_connected\_tiles  Amount

Game versions: DE only

Requires: objects being placed in groups

Arguments:

* Amount - number (default: 0)

Prevents grouped objects from being placed in an area with fewer tiles than the specified amount.  Intended to be used to keep objects off tiny islands and out of tiny forest clearings.

* BUG: Objects will be extremely biased towards being placed in the top left of the map, making this attribute useless for the intended purpose.  (Use [max\_distance\_to\_other\_zones](#h.qf90qwpxyzrs) or [avoid\_forest\_zone](#h.ym7v1j9vbnle) instead).

Example: Create many groups of sheep that avoid small forest clearings and only appear in the top half of the map.

<LAND\_GENERATION>

base\_terrain  BAMBOO

create\_player\_lands {

    land\_percent 50

    border\_fuzziness 1

    left\_border 25    right\_border 25    top\_border 25    bottom\_border 25

    zone 1

}

<OBJECTS\_GENERATION>

create\_object SHEEP {

    number\_of\_objects 4

    set\_tight\_grouping

    number\_of\_groups 150

    min\_connected\_tiles 80

}

### resource\_delta  Amount

Game versions: UP/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493368812&usg=AOvVaw3yL_YlLJQ_FNV0GgvUOTm0)

Arguments:

* Amount - number (default: 0)

* In UP, resource amount will overflow past 32767
* In DE, resource amount will overflow past 2147483647 (but will become inaccurate before then)
* Negative values can be used to reduce the resources

Modify the amount of food/wood/gold/stone in an object.

* Does not work for farms.
* Does not appear when testing a map from the scenario editor.
* You can give food to wolves.  However, if a villager runs into and kills a wolf, they will automatically gather the food (instead of doing whatever you sent them to do) - so this is not great for gameplay.

Example: Create gold piles that have 100 less gold in them and stone mines with 100 more stone.

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_objects 7

resource\_delta -100

}

create\_object STONE {

number\_of\_objects 7

        resource\_delta 100

}

### second\_object  ObjectType

Game versions: DE only

Arguments:

* ObjectType - object constant (see: [Objects](#h.nvxriamulybh))

Specify ANY object to be placed on top of the main object.

* If you are placing multiple objects, each will get the specified second object.
* In the official maps, it used to place villagers on top of farms for empire wars.
* second\_object can be used to bypass terrain restrictions by using an invisible placeholder object as the main object.

* For off-grid placeholders, any dead unit can be used, especially dead heroes that are without graphics in DE (for example, ID 647).
* For on-grid placeholders, try the terrain blocker (ID 1613) or the dead fish trap (ID 278), or a berry bush with zero food (using [resource\_delta](#h.ndaw6icg9cnp)). (DO NOT USE object 1291, as a recent update made it so that this object will now permanently convert player sheep to gaia).
* Alternatively, terrain restrictions of an object can be changed with [effect\_amount](#h.1niw1edwqhy5) or removed entirely with [ignore\_terrain\_restrictions](#h.fx1jh8glz0tl)

Example: Players start with a cow underneath their town center.

<OBJECTS\_GENERATION>

create\_object TOWN\_CENTER {

set\_place\_for\_every\_player

max\_distance\_to\_players 0

second\_object DLC\_COW

}

### set\_scaling\_to\_map\_size

Game versions: All

Mutually exclusive with: [set\_scaling\_to\_player\_number](#h.l48a16uing0q)

Scales [number\_of\_groups](#h.t7eg3wg2xm3w) to the map size.  Unscaled value refers to a 100x100 map (see: [Map Sizes](#h.qannz915qgy5) for the scaling table)

* If no grouping is present, scaling applies to [number\_of\_objects](#h.btcx5h61er65) instead.

Example: Create clumps of 10 gold and scale the number of groups to map size.

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_objects 10

number\_of\_groups 3

set\_scaling\_to\_map\_size

set\_tight\_grouping

}

### set\_scaling\_to\_player\_number

Game versions: All

Mutually exclusive with: [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)

Scales [number\_of\_groups](#h.t7eg3wg2xm3w) to player count. This means x2 for a 2-player game and x8 for an 8-player game.

* If no grouping is present, scaling applies to [number\_of\_objects](#h.btcx5h61er65) instead.

Example: Scale the number of relics by the number of players

create\_object RELIC {

number\_of\_objects 2

set\_scaling\_to\_player\_number

}

### set\_place\_for\_every\_player

Game versions: All

Mutually exclusive with: [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

Place the object(s) as a personal object for each player (actually for each [player land](#h.esy5dq29i0wr)).  Objects that cannot be owned by players (boar, gold, trees, etc.) also require [set\_gaia\_object\_only](#h.bnzkfqaopnv9) to be placed for every player.

* Only works for player lands or lands assigned to players.  Disabled by [land\_id](#h.c97q6t5q24lj)
* Objects will only be placed where they are not separated from the origin of their land by a terrain they are restricted on, unless [ignore\_terrain\_restrictions](#h.fx1jh8glz0tl) is used.

* This means that on islands your resources will only end up on your own island
* It also means that player gold mines on acropolis can only be placed on the hilltops, because gold is restricted from the rock terrain.
* Water objects (docks/boats) CAN be placed if the player land is made of a dirt terrain type.
* Terrain restrictions can be bypassed by using a placeholder and [second\_object](#h.cr71z3stu8pd) or modified with [effect\_amount](#h.1niw1edwqhy5) or removed with [ignore\_terrain\_restrictions](#h.fx1jh8glz0tl)
* Even though road terrains are restricted for resources, they do not form a separation the way other terrains do.

Example: Give every player their starting villagers.

create\_object VILLAGER {

set\_place\_for\_every\_player

min\_distance\_to\_players 6

max\_distance\_to\_players 7

}

### place\_on\_specific\_land\_id  Identifier

Game versions: All

Mutually exclusive with: [set\_place\_for\_every\_player](#h.hch89ipgsvb)

Arguments:

* Identifier - number

Place the object(s) on each land of the specified identifier.  IDs are set in [<LAND\_GENERATION>](#h.15g4dj26anlp) by using the [land\_id](#h.c97q6t5q24lj) attribute.

* Objects will only be placed where they are not separated from the origin of their land by a terrain they are restricted on, unless [ignore\_terrain\_restrictions](#h.fx1jh8glz0tl) is used.

* Even though road terrains are restricted for resources, they do not form a separation the way other terrains do.

* If multiple lands have the same ID, the object(s) will be placed on all relevant lands.

Example: Create a tiny snowy land and place a gold mine on it.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

        terrain\_type DIRT

        land\_percent 0

}

create\_land {

terrain\_type SNOW

land\_percent 0

land\_id 13

land\_position 50 50

}

<OBJECTS\_GENERATION>

create\_object GOLD {

place\_on\_specific\_land\_id 13

find\_closest

}

### generate\_for\_first\_land\_only

Game versions: DE only

Requires: [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

If there are multiple [create\_player\_lands](#h.esy5dq29i0wr) commands or multiple lands sharing a [land\_id](#h.c97q6t5q24lj), this object will only be placed on the first applicable land, instead of on all of them.

Example: Generate two lands for each player and give each player a house on both of them but a king only on one of them.

<LAND\_GENERATION>

base\_terrain WATER

create\_player\_lands {

    land\_percent 10

}

create\_player\_lands {

    land\_percent 10

}

<OBJECTS\_GENERATION>

create\_object HOUSE {

    set\_place\_for\_every\_player

}

create\_object KING {

    set\_place\_for\_every\_player

    generate\_for\_first\_land\_only

}

### set\_gaia\_object\_only

Game versions: All

Use with [set\_place\_for\_every\_player](#h.hch89ipgsvb) to place gaia (neutral) objects on a per-player basis.  Must be used when placing player's gold/stone/berries/deer/boar.

* Can be used for controllable objects (for example, sheep)
* Units and buildings will permanently join the player who first finds them, unless [set\_gaia\_unconvertible](#h.g4mzdyb4izbo) is also specified.
* Gaia building architectural style can be changed with [set\_gaia\_civilization](#h.yy69o1bqyfx5)

Example: Give every player four gaia sheep close to their starting town.

<OBJECTS\_GENERATION>

create\_object SHEEP {

number\_of\_objects 4

set\_loose\_grouping

set\_gaia\_object\_only

set\_place\_for\_every\_player

min\_distance\_to\_players 7

max\_distance\_to\_players 8

}

### set\_gaia\_unconvertible

Game versions: DE only

Requires: [set\_gaia\_object\_only](#h.bnzkfqaopnv9)

Mutually exclusive with: [set\_building\_captureable](#h.svu8loj25dpl)

Use with any gaia object to make that object unrescuable by players and hostile towards them.

* Must be used after [set\_gaia\_object\_only](#h.bnzkfqaopnv9)
* Note that gaia military units will act as if they were on defensive stance - attacking anything that enters their search radius and retreating if you run away.
* Does not work when testing from the scenario editor.
* Unrescuable status does not apply to [second\_object](#h.cr71z3stu8pd)
* Certain objects are always convertible (ie. monuments) or buggy (town centers, gates).
* Gaia markets lose functionality, and cannot be traded with.

* Use object 1646 to give gaia an indestructible market for players to trade with.

* Villagers will repair gaia buildings, rather than attack them.

Example: Decorate the map with unrescuable gaia pyramids.

<OBJECTS\_GENERATION>

create\_object PYRAMID {

number\_of\_objects 3

set\_gaia\_object\_only

set\_gaia\_unconvertible

make\_indestructible

}

### set\_building\_capturable

Game versions: DE only

Mutually exclusive with: [set\_gaia\_unconverible](#h.g4mzdyb4izbo)

Used to make a building switch control to whoever most recently has units nearby.

* Has no effect on units or other non-building objects.

* Can be used for buildings that start under gaia control or under player control.
* Capturable buildings cannot be deleted.
* Capturable buildings can be destroyed (unless [make\_indestructible](#h.a9ken9hkekd6) is used).

Example: Place an outpost on the map that will convert to the control of whoever is currently nearby.

<OBJECTS\_GENERATION>

create\_object OUTPOST {

    set\_gaia\_object\_only

    make\_indestructible

    set\_building\_capturable

}

### make\_indestructible

Game versions: DE only

Make a building indestructible.  The building receives 9999 HP, 1000/1000 armor, and cannot be attacked, damaged or deleted.

* Has no effect on units or other non-building objects.
* Can be used to make neutral gaia markets, docks, or whole cities that cannot be attacked.

Example: Make the starting town center indestructible.  (Note that this will mean that players cannot be defeated)

create\_object TOWN\_CENTER {

set\_place\_for\_every\_player

max\_distance\_to\_players 0

make\_indestructible

}

### min\_distance\_to\_players  Distance

### max\_distance\_to\_players  Distance

Game versions: All

Arguments:

* Distance - number (default: no limits)

* If max is negative, no limits apply
* If min exceeds max, no objects are placed

Minimum and maximum distance (in tiles) from the origin of player lands, that the object can be placed.

* It is not necessary to specify both attributes.
* Distances are a square, not a circle, unless [set\_circular\_placement](#h.15fez3e52vqr) is specified.
* If the objects are grouped, distance refers to the center of the group, not the individual group members.
* When used with [place\_on\_specific\_land\_id](#h.34wzlujx4lbv), distances refer to that specific land.
* When used without [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv), maximum distance has no effect.
* BUG (DE): When used with [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv), minimum distance applies to ALL lands, not just player lands (or the specific ID).  If your map has too many non-player lands to effectively use min\_distance\_to\_players, an alternative is to create an [actor\_area](#h.obv5ypy66a57) of the desired radius (or several of different radii) on the player lands and then have the objects avoid that actor area.FIXED in April 2025!
* BUG:  If distances are very constrained (ie. min=max), objects are noticeably biased towards being placed in the west (ie. starting villagers).
* BUG (pre-DE): minimum distance ALWAYS applies to ALL lands.

Example: Place the starting scout at a distance of 7-9 tiles.

<OBJECTS\_GENERATION>

create\_object SCOUT {

set\_place\_for\_every\_player

min\_distance\_to\_players 7

max\_distance\_to\_players 9

}

### set\_circular\_placement

Game versions: DE only

Changes [min\_distance\_to\_players](#h.asuv2zzhmbsd) and [max\_distance\_to\_players](#h.v2aq68odkdzl) to use the circular (Euclidean) distance, rather than a square radius.  This prevents resources on the diagonal from being very far away.

* This probably should be used for most player objects to improve resource spawns, unless walls are present (since walls are traditionally square).
* Additionally, if used for a group of objects with [set\_loose\_grouping](#h.umboa0q57v9y), the area of [group\_placement\_radius](#h.675xoyq748tw) will be a circle instead of a square.

Example: Use circular placement on the distances for player sheep spawns.

<OBJECTS\_GENERATION>

create\_object SHEEP {

number\_of\_objects 2

number\_of\_groups 2

set\_gaia\_object\_only

set\_place\_for\_every\_player

min\_distance\_to\_players 18

max\_distance\_to\_players 23

set\_circular\_placement

}

### terrain\_to\_place\_on  TerrainType

Game versions: All

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: any valid terrain)

The object(s) will only be placed on the specified terrain.

Example: Place decorative rocks on a central desert.

<LAND\_GENERATION>

create\_land {

terrain\_type DESERT

number\_of\_tiles 500

land\_position 50 50

}

<OBJECTS\_GENERATION>

create\_object ROCK {

number\_of\_objects 300

terrain\_to\_place\_on DESERT

}

### layer\_to\_place\_on  TerrainType

Game versions: DE only

Arguments:

* TerrainType - terrain constant (see: [Terrains](#h.3bdjnf7tryyk)) (default: any layer)

The object(s) will only be placed on the specified layering terrain.

* Works for [terrain\_mask](#h.e0ug99qovffm) 1, but not when set to 2.  In that case you must use [terrain\_to\_place\_on](#h.t7m0dcvh1px) instead, because the layer has become the main terrain.
* If used together with [terrain\_to\_place\_on](#h.t7m0dcvh1px), the object(s) will be placed only where both the base terrain and the layer apply.

Example: Place rocks on a small patch of layered snow within a larger desert area.

<LAND\_GENERATION>

create\_land {

terrain\_type DESERT

number\_of\_tiles 500

land\_position 50 50

}

<TERRAIN\_GENERATION>

create\_terrain SNOW {

    base\_terrain DESERT

    number\_of\_tiles 20

    terrain\_mask 1

}

<OBJECTS\_GENERATION>

create\_object ROCK {

number\_of\_objects 300

layer\_to\_place\_on DESERT

}

### ignore\_terrain\_restrictions

Game versions: DE only

Requires: [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

Objects can be placed on terrains they are normally restricted from, and these terrains no longer constitute a border on their placement.  Must be used with [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [set\_place\_on\_specific\_land\_id](#h.34wzlujx4lbv).

* Can be used in combination with [terrain\_to\_place\_on](#h.t7m0dcvh1px)
* You can instead modify ATTR\_TERRAIN\_ID with [effect\_amount](#h.1niw1edwqhy5) to change the terrain restrictions of any object, or use [second\_object](#h.cr71z3stu8pd) with a placeholder.

Example: Place salmon on the land near each player's town center.  (Fish are can normally only be placed on water terrains)

create\_object SALMON {

number\_of\_objects 4

set\_place\_for\_every\_player

min\_distance\_to\_players 3

set\_gaia\_object\_only

find\_closest

ignore\_terrain\_restrictions

}

### max\_distance\_to\_other\_zones  Distance

Game versions: All

Arguments:

* Distance - number (default: 0)

Minimum (NOT maximum) distance, in tiles, that objects will stay away from terrains that they are restricted from being placed on.

* Useful for keeping resources away from coastlines, or deep fish away from beaches.
* If the objects are grouped, distance refers to the center of the group, not the individual members.
* Does not apply to road terrains, even though resources cannot be placed on them.
* Useless for objects without any terrain restrictions.

Example: Place a central lake and then fill the map with gold that avoids being close to water.

<LAND\_GENERATION>

create\_land {

terrain\_type WATER

number\_of\_tiles 500

land\_position 50 50

}

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_groups 9000

set\_gaia\_object\_only

max\_distance\_to\_other\_zones 5

}

### place\_on\_forest\_zone

Game versions: DE only

Mutually exclusive with: [avoid\_forest\_zone](#h.ym7v1j9vbnle)

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493401570&usg=AOvVaw1HOFQaxaLsuVTriirUaAuh)

Place objects only on, and directly next to, tiles with trees on them (including straggler trees and scenario editor trees).

Example: Place sheep all along the edge of forests.

<OBJECTS\_GENERATION>

create\_object SHEEP {

number\_of\_objects 99999

place\_on\_forest\_zone

}

### avoid\_forest\_zone  Distance

Game versions: DE only

Mutually exclusive with: [place\_on\_forest\_zone](#h.38vodsu87lbp)

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493402737&usg=AOvVaw2u-q2jhMjEi6eiRMi0Ma5A)

Arguments:

* Distance - number (default: no avoidance)

* Defaults to 1 if you specify the argument but omit the distance.

Objects will stay the specified number of tiles away from any trees (including straggler trees and scenario editor trees)

* Used to keep resources away from forests.
* Note that the forest trees themselves are being avoided, so for sparse forests (especially baobab) larger distances may be necessary.
* If the objects are grouped, distance will apply to the individual group members.

Example: Fill the map with gold, except for the areas near trees.

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_groups 99999

avoid\_forest\_zone 3

}

### avoid\_cliff\_zone  Distance

Game versions: DE only

Arguments:

* Distance - number (default: no avoidance)

* Defaults to 1 if you specify the argument but omit the distance.

Objects will stay the specified number of tiles away from cliffs.  Note that because of the size of the cliff objects, you need to specify at least a distance of 2 to actually create a gap between the cliffs and the object(s).

* Useful for preventing inaccessible resources.
* If the objects are grouped, distance will apply to the individual group members.

Example: Fill the map with stone that stays 3 tiles away from cliffs.

<CLIFF\_GENERATION>

<OBJECTS\_GENERATION>

create\_object STONE {

number\_of\_groups 99999

avoid\_cliff\_zone 4

}

### min\_distance\_to\_map\_edge  Distance

Game versions: DE only

Arguments:

* Distance - number (default: 0)

Minimum distance, in tiles, that objects will stay away from the edge of the map.

* If the objects are grouped, distance refers to the center of the group, not the individual members.

Example: Ensure that relics stay at least 10 tiles from the edge of the map.

<OBJECTS\_GENERATION>

create\_object RELIC {

set\_gaia\_object\_only

number\_of\_objects 500

min\_distance\_to\_map\_edge 10

}

### min\_distance\_group\_placement  Distance

Game versions: All

Arguments:

* Distance - number (default: 0)

Minimum distance, in tiles, that individual objects of the same [create\_object](#h.2vz7nxt2afqo) command, and ALL future objects, must stay away from each object.

* Best used with small values, to keep different resources from being directly next to each other.
* To scatter objects from the same command far away from each other, use [temp\_min\_distance\_group\_placement](#h.a5n8aue3ffi4)
* If the objects are grouped, distance refers to the center of the group, not the individual members.

Example: Give each player two sets of forages and make them avoid each other by 4 tiles, and keep all future objects 4 tiles away.

<OBJECTS\_GENERATION>

create\_object FORAGE {

number\_of\_objects 7

number\_of\_groups 2

set\_tight\_grouping

set\_place\_for\_every\_player

set\_gaia\_object\_only

min\_distance\_to\_players 8

max\_distance\_to\_players 10

min\_distance\_group\_placement 4

}

### temp\_min\_distance\_group\_placement  Distance

Game versions: All

Arguments:

* Distance - number (default: 0)

Like [min\_distance\_group\_placement](#h.b2u5jna014lf), but only applies to the current [create\_object](#h.2vz7nxt2afqo) command - future objects are unaffected.

* Useful for scattering objects, for example neutral resources and relics.
* Can be used together with [min\_distance\_group\_placement](#h.b2u5jna014lf)
* If the objects are grouped, distance refers to the center of the group, not the individual members.

Example: Scatter neutral gold evenly across the map.

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_groups 9320

number\_of\_objects 4

set\_gaia\_object\_only

set\_tight\_grouping

min\_distance\_group\_placement 4

temp\_min\_distance\_group\_placement 46

}

### find\_closest

Game versions: DE only

Requires: [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493411350&usg=AOvVaw2nTdDzCwcqqv82tQ92UqcB)

Place the object on the closest free tile to the center of the land, taking into consideration all other constraints.

* IMPORTANT: find\_closest uses the circular (Euclidean) distance, while all other distance constraints (ie. [min\_distance\_to\_players](#h.asuv2zzhmbsd)) use a square distance by default.

* As a result, using both find\_closest and [min\_distance\_to\_players](#h.asuv2zzhmbsd) (without further constraints) will often place objects at 90° to each other because the corners of the square are further from the center than the edges.  Use [set\_circular\_placement](#h.15fez3e52vqr) combined with [enable\_tile\_shuffling](#h.ewsg05tiznb0) to solve this issue.

* Bug: When using find\_closest in reference to a land origin, previously that would place the object directly on the origin (assuming no other restrictions), but now it places it one tile away.  Use [max\_distance\_to\_players](#h.v2aq68odkdzl) 0 if you need the object right on the origin.

Example: Give each player a fishing ship on the closest free water tile.

<OBJECTS\_GENERATION>

create\_object FISHING\_SHIP {

set\_place\_for\_every\_player

ignore\_terrain\_restrictions

terrain\_to\_place\_on WATER

find\_closest

}

### find\_closest\_to\_map\_center

Game versions: DE only

Requires: [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

Place the object on the closest free tile to the center of the map, taking into consideration all other constraints.

* Overridden by [find\_closest](#h.kzkb7o2yhtk9)
* Bug: When using find\_closest\_to\_map\_center for loosely grouped objects, some group members may fail to spawn if the closest free area is too small.  [Detailed bug description](https://www.google.com/url?q=https://forums.ageofempires.com/t/usage-of-find-closest-and-set-loose-grouping-in-map-scripts/221258&sa=D&source=editors&ust=1744981493414185&usg=AOvVaw0km2rrI4cz2-Y1h1cFYHnS)

Example: Place a boar in the map center for each player.

<OBJECTS\_GENERATION>

create\_object BOAR {

set\_place\_for\_every\_player

set\_gaia\_object\_only

find\_closest\_to\_map\_center

}

### find\_closest\_to\_map\_edge

Game versions: DE only

Requires: [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

Place the object on the closest free tile to the edge of the map, taking into consideration all other constraints.

* Overridden by [find\_closest](#h.kzkb7o2yhtk9) and [find\_closest\_to\_map\_center](#h.c8jwpxwfx68p)
* Bug: When using find\_closest\_to\_map\_edge for loosely grouped objects, some group members may fail to spawn if the closest free area is too small.  [Detailed bug description](https://www.google.com/url?q=https://forums.ageofempires.com/t/usage-of-find-closest-and-set-loose-grouping-in-map-scripts/221258&sa=D&source=editors&ust=1744981493415972&usg=AOvVaw3KGolpzj_d8zRChcCP5pMU)

Example: Place a relic on the map edge for each player.

<OBJECTS\_GENERATION>

create\_object RELIC {

set\_place\_for\_every\_player

set\_gaia\_object\_only

find\_closest\_to\_map\_edge

}

### require\_path Deviation

Game versions: DE only

Requires: [set\_place\_for\_every\_player](#h.hch89ipgsvb) or [place\_on\_specific\_land\_id](#h.34wzlujx4lbv)

Arguments:

* Deviation - number (default: 0)

* 0 = indirect paths allowed
* 1 = only direct paths
* >1 = more deviation from the direct path allowed

Objects with this attribute must have a path to the origin of their associated land.  Use this attribute to prevent player resources from being trapped in or behind forests.

* No argument, or a value of 0 imposes no further restrictions.
* An argument of 1 means that the object must additionally have a mostly direct path to the origin.
* Larger values allow paths that are less direct. Maximum effective value depends on how constricted the path is.

Example: Make sure a player boar isn't trapped behind nearby woodlines.

<OBJECTS\_GENERATION>

create\_object BOAR {

        set\_place\_for\_every\_player

        set\_gaia\_object\_only

        require\_path 1

        min\_distance\_to\_players 16

        max\_distance\_to\_players 22

}

### force\_placement

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493419892&usg=AOvVaw2cphC0_TkOd0B_PN90Ur-D)

Allows multiple objects to be placed on the same tile at once, if necessary.  Normally, objects are placed one per tile, and if the tiles run out, no more objects are placed.  With force\_placement active, when tiles run out, the remaining objects are placed on the corners of tiles, and then on top of each other.

* Only works for objects that can overlap on the same tile (ie. units, but not buildings)
* Disabled when using [set\_loose\_grouping](#h.umboa0q57v9y)

Example: Place 50 sheep in the 1-tile radius surrounding a starting outpost.

<OBJECTS\_GENERATION>

create\_object OUTPOST {

set\_place\_for\_every\_player

max\_distance\_to\_players 0

}

create\_object SHEEP {

number\_of\_objects 50

set\_place\_for\_every\_player

max\_distance\_to\_players 1

force\_placement

}

### actor\_area  Identifier

Game versions: DE only

See also: [create\_actor\_area](#h.u28jmnfojke3)

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493422196&usg=AOvVaw1oNYr8evzBpBK1t5xyLq-g)

Arguments:

* Identifier - number (default: 0 - no actor area)

Specifies a numerical identifier which can be referred to in future objects with [avoid\_actor\_area](#h.cgoa0e8x398u) or [actor\_area\_to\_place\_in](#h.d6d6k8uc57zx)

Example: Spawn a wolf next to each relic.

<OBJECTS\_GENERATION>

create\_object RELIC {

number\_of\_objects 5

set\_gaia\_object\_only

temp\_min\_distance\_group\_placement 35

actor\_area 1234

}

create\_object WOLF {

number\_of\_objects 9320

set\_gaia\_object\_only

actor\_area\_to\_place\_in 1234

temp\_min\_distance\_group\_placement 25

}

### actor\_area\_radius  Radius

Game versions: DE only

Requires: [actor\_area](#h.obv5ypy66a57)

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493424757&usg=AOvVaw1U3PlZ_Zz23vf1tUW9bB4O)

Arguments:

* Radius - number (default: 1 = 3x3 area)

Used with [actor\_area](#h.obv5ypy66a57) to specify how large it should be.

Example: Give each player a mill with 7 deer in a 7-tile radius.

<OBJECTS\_GENERATION>

create\_object MILL {

set\_place\_for\_every\_player

min\_distance\_to\_players 16

max\_distance\_to\_players 20

actor\_area 61

actor\_area\_radius 7

}

create\_object DEER {

number\_of\_objects 7

set\_place\_for\_every\_player

set\_gaia\_object\_only

actor\_area\_to\_place\_in 61

}

### override\_actor\_radius\_if\_required

Game versions: DE only

Requires: [actor\_area\_to\_place\_in](#h.d6d6k8uc57zx)

Prevents buildings from overlapping when placed in an [actor\_area](#h.obv5ypy66a57) with a radius that is too small to contain them, by expanding the valid placement area outwards.

* Used in the official maps for mills in Empire Wars to ensure they are placed properly when they become folwarks for the Poles civilization.
* Does not seem to work on units.

Example: Place a barracks with the default actor\_area\_radius of 1, and then place a house adjacent, and prevent it from overlapping the barracks.

<OBJECTS\_GENERATION>

create\_object BARRACKS {

    set\_place\_for\_every\_player

    find\_closest

    actor\_area 2

}

create\_object HOUSE {

    set\_place\_for\_every\_player

    actor\_area\_to\_place\_in 2

    override\_actor\_radius\_if\_required

}

### actor\_area\_to\_place\_in  Identifier

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493428314&usg=AOvVaw2-rAREsZyjFoRQnaxx0gNN)

Arguments:

* Identifier - number

Place the object only within the radius of the specified [actor\_area](#h.obv5ypy66a57) or [create\_actor\_area](#h.u28jmnfojke3)

* The same object can only have one actor\_area\_to\_place\_in.
* Actor areas have some intricacies that can affect placement.  If you are having issues, follow these guidelines:

* Different objects can be assigned to the same actor area
* Do not place origin-referenced (either player or land id) objects in generic actor areas
* Placing generic objects into land id-referenced actor areas always works
* Placing player objects into land id-referenced actor areas always works
* Only player objects should be placed into player-referenced actor areas
* When placing generic objects in generic actor areas, try to have the fewest create object commands possible between the actor area creation and the object to be placed in it.
* When none of the rules can be satisfied, inverse actor areas can be used as a failsafe

Example: Place a lumber camp on the nearest forest and place villagers there too.

<OBJECTS\_GENERATION>

create\_object LUMBER\_CAMP {

set\_place\_for\_every\_player

max\_distance\_to\_players 67

place\_on\_forest\_zone

find\_closest

actor\_area 8

actor\_area\_radius 4

}

create\_object VILLAGER {

set\_place\_for\_every\_player

number\_of\_objects 4

actor\_area\_to\_place\_in 8

place\_on\_forest\_zone

find\_closest

}

### avoid\_actor\_area  Identifier

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493431166&usg=AOvVaw0SQS5ivendq6ZbWx15a6Hx)

Arguments:

* Identifier - number

The object will avoid the specified [actor\_area](#h.obv5ypy66a57) or [create\_actor\_area](#h.u28jmnfojke3)

* The same object can avoid multiple actor areas.
* You can specify an [actor\_area](#h.obv5ypy66a57) and then avoid that same actor area within the same [generate\_object](#h.2vz7nxt2afqo) statement.  However, this only works with ungrouped objects, or those with [set\_loose\_grouping](#h.umboa0q57v9y)

Example: Place a barracks for empire wars but have it avoid various other objects that you already placed.

<OBJECTS\_GENERATION>

create\_object BARRACKS {

set\_place\_for\_every\_player

min\_distance\_to\_players 7

max\_distance\_to\_players 9

avoid\_actor\_area 94

avoid\_actor\_area 40

avoid\_actor\_area 8

avoid\_actor\_area 9

avoid\_actor\_area 99

avoid\_actor\_area 171

actor\_area 51

actor\_area\_radius 5

}

### avoid\_all\_actor\_areas

Game versions: DE only

External reference: [Official DE Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493433034&usg=AOvVaw28iRiOsx7XjAeW8xnZkcaR)

The object will avoid being placed within ANY existing [actor\_area](#h.obv5ypy66a57) or [create\_actor\_area](#h.u28jmnfojke3)

Example: Place wolves that avoid all actor areas.

<OBJECTS\_GENERATION>

create\_object TOWN\_CENTER {

set\_place\_for\_every\_player

max\_distance\_to\_players 0

actor\_area 100

actor\_area\_radius 60

}

create\_object WOLF {

number\_of\_objects 9320

temp\_min\_distance\_group\_placement 52

avoid\_all\_actor\_areas

}

### enable\_tile\_shuffling

Game versions: DE only

Increases randomness of object positions by shuffling the list of candidate tiles rather than just using the first entry.

* When using both [find\_closest](#h.kzkb7o2yhtk9) and [set\_circular\_placement](#h.15fez3e52vqr), add this attribute to prevent objects from being in predictable positions.
* Does not prevent the bias towards the west when [min\_distance\_to\_players](#h.v2aq68odkdzl) and [max\_distance\_to\_players](#h.v2aq68odkdzl) are close or equal.
* Should NOT be used when attempting to place objects in a specific precise location (ie. placing herdables or villagers under the town center.)

Example: Create 4 individual gold mines randomly positioned in a circle around players, with no bias towards any position.

<OBJECTS\_GENERATION>

create\_object GOLD {

set\_place\_for\_every\_player

set\_gaia\_object\_only

number\_of\_objects 4

min\_distance\_to\_players 12

set\_circular\_placement

find\_closest

enable\_tile\_shuffling

}

### set\_facet FacetNumber

Game versions: DE only

Arguments:

* FacetNumber - number (default: 0 - random facet)

* FacetNumber corresponds to the index - 1 of the desired frame in the sprite.
* To get the first frame, pick a facet number below 0, or above the maximum for that object.

Choose which frame (of the sprite) of an object to generate.

* For units, this corresponds to the angle they are facing.
* For other objects, this may correspond to alternative appearances.
* Facets can be cycled by using the rotate feature in the scenario editor.
* Frames can be viewed using external tools such as [SLX Studio](https://www.google.com/url?q=https://aok.heavengames.com/blacksmith/showfile.php?fileid%3D13179&sa=D&source=editors&ust=1744981493436690&usg=AOvVaw0GtSP3NlkrUHiWpTogopEV).

Example: Generate 10 jungle straggler trees that all look identical and have the appearance of frame n\_tree\_jungle\_x1\_031 (a large and small palm tree)

create\_object JUNGLETREE {

    number\_of\_objects 10

    set\_facet 30

}

### match\_player\_civ

Game versions: [Star Wars Galactic Battlegrounds](https://www.google.com/url?q=https://store.steampowered.com/app/356500/STAR_WARS_Galactic_Battlegrounds_Saga/&sa=D&source=editors&ust=1744981493437442&usg=AOvVaw3qcb0WTN9mZ7Ylw-21WXco) only!!!

Used to ensure that each faction gets their correct starting scout unit.

* With the exception of this attribute, SWGB uses the same commands and attributes that are available in AoC.
* Usually used for the starting scout, but also works for other units such as unique units from the fortress.

---

##

## Global Syntax

There are some additional pieces of syntax that can be used across all sections.

## Comments

A comment is a piece of text that is ignored by the parser, but provides helpful information to someone looking at the code, such as yourself.

* Comments can be nested.  If you have a comment within a comment, the "sub comment" will not prematurely terminate the main comment, even if syntax highlighters indicate elsewise.
* Make sure to always include a separator between the comment character and the comment text.  This is a common mistake, and many syntax highlighters will not properly recognize broken comments.
* BUG (pre-DE): Comments within dead branches (see: [Conditionals](#h.crt6psej7mdo) and [Random Code](#h.87mv66lnefdm)) are NOT ignored.  For more information, see this external article: [Parser Pitfalls](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42304,,365&sa=D&source=editors&ust=1744981493439178&usg=AOvVaw3M1pXIvq98ZHVR8op02DK7)

Examples: Working comments

/\* this is a comment \*/

/\*

this is a comment

\*/

/\* this is a

multi-line comment

\*/

/\* /\* this is a nested \*/ comment \*/

Example: Broken comments

// this is NOT a comment

#this is NOT a comment

```this is NOT a comment```

/\*this is NOT a comment\*/

/\*\*\* this is NOT a comment \*\*\*/

/\* this comment never ends

/\* this comment never ends\*/

/\* this comment never ends \*/\*

---

##

## Including Other Files

The standard maps include shared files for the resource generation.

* In AoC/UP this is found within the gamedata\_x1.drs file.  You can open the drs file with any text editor and look for the relevant part.
* In vanilla HD you can find the land\_resources.inc file in the gamedata\_x1 folder.
* In DE you can find the GeneratingObjects.inc file in the gamedata\_x2 folder.  Additionally you can find shared files for seasons, elevation, animals, water mixing, etc.

The file random\_map.def is always included, without having to specify it.  It contains all the predefined constants.

VERY IMPORTANT:  Included rms files are NOT transferred in the lobby!  This means:

* You CAN include any of the standard files that are part of the game, because other players will already have them in their directory.
* You CANNOT include custom files, unless everyone in the lobby has the file.  So you can include custom files with full conversion mods, because all players will need to have the mod to be able to play in the first place.

### #include\_drs  Filename

Game versions: HD/DE (in AoC it is used for the built-in maps, but doesn't seem to work for custom maps)

Arguments:

* Filename - name (or path and name)

* Valid file extensions are: rms, rms2, inc, def
* You can navigate to a parent directory with ../
* If your path or filename contains spaces, you can surround it with quotation marks: "this is the/path to/example file name.rms"

Include a file located in the gamedata folder.

* If you include a file somewhere else, the file path must be relative to the gamedata folder.

Example: Include the DE seasons file, so that you can use it in your own script, without having to set up your own terrains.

#include\_drs F\_seasons.inc

Example2: Include that classic land and water resources file from AoC.

<OBJECTS\_GENERATION>

#include\_drs land\_and\_water\_resources.inc

Example3: Make a custom version of blind random.

start\_random

percent\_chance 20        #include\_drs Arabia.rms

percent\_chance 20        #include\_drs Baltic.rms

percent\_chance 20        #include\_drs Gold\_Rush.rms

percent\_chance 20        #include\_drs Islands.rms

percent\_chance 20        #include\_drs Team\_Islands.rms

end\_random

### #includeXS  Filename

Game versions: DE only

External reference: [.xs scripting in Age of Empires II: Definitive Edition](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/xs-scripting-in-age-of-empires-ii-definitive-edition&sa=D&source=editors&ust=1744981493444206&usg=AOvVaw2Xd6hxtI1ak75p-Y9reE9q), [XS Scripting For Beginners](https://www.google.com/url?q=https://ugc.aoe2.rocks/general/xs/&sa=D&source=editors&ust=1744981493444372&usg=AOvVaw347Vy_5t2Ski-dAlsRVFbq)

Arguments:

* Filename - name (or path and name)

* Valid file extensions are: xs
* You can navigate to a parent directory with ../
* BUG:  You cannot surround your path with quotation marks

Include an xs file, located in the xs folder.

* If you include a file somewhere else, the file path must be relative to the xs folder.
* The path can also be relative to the xs folder in player profile, rather than to the xs folder in the main game directory.
* Unlike included rms files, included XS files DO transfer automatically to players and spectators.

Examples: [XS Scripting For Beginners](https://www.google.com/url?q=https://ugc.aoe2.rocks/general/xs/&sa=D&source=editors&ust=1744981493445506&usg=AOvVaw1CKe9ks_kj7tVagWEvtskL)

---

##

## Random Code

Can be used just about anywhere to add an element of randomness to your script.

### start\_random

### percent\_chance  %  Code

### end\_random

Game versions: All

Arguments:

* % - number (0-99)
* Code - anything

Specify a piece of code that has a defined chance of being chosen.

* If the total percentages add up to less than 99%, there is a chance that none of them get chosen.
* If the total exceeds 99%, only the first 99% will have a chance of occurring.
* Random constructs can encompass individual arguments, or even whole blocks of code.
* They cannot be nested.  To achieve a non-integer chance, use a first random block to define (using [#define](#h.hhofpn9iwfxi)) which additional random block to run.
* BUG: if the first branch is percent\_chance 0, it is still chosen occasionally.  Do not include a percent\_chance 0 as the first branch.  Also note that the 100th percent is never chosen.
* BUG (AoC/HD/UP): Comments in dead branches are not ignored.  Do not include any random syntax (ie. end\_random) in such comments.  For more information, see this external article: [Parser Pitfalls](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42304,,365&sa=D&source=editors&ust=1744981493447478&usg=AOvVaw3VbByJ-R3uV5Q2ihQGJzer)

Example:  Place 5 or 6 or 7 gold mines with 6 being the most likely.

<OBJECTS\_GENERATION>

create\_object GOLD {

start\_random

percent\_chance 30        number\_of\_objects 5

percent\_chance 50        number\_of\_objects 6

percent\_chance 20        number\_of\_objects 7

end\_random

}

Example2:  Have a 10% chance of placing 5 gold mines (and a 90% of not doing so)

<OBJECTS\_GENERATION>

start\_random

percent\_chance 10

create\_object GOLD {

number\_of\_objects 5

}

end\_random

### rnd(min,max)

Game versions: UP/DE

External reference: [UserPatch Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493449082&usg=AOvVaw1-Nf5gbC13p4SeQhvEOqa2)

Arguments:

* min - number
* max - number

Randomize a numeric argument between min and max (inclusive).

* Make sure there are no spaces in the whole construct.
* Make sure max exceeds min.

Example:  Place 5 or 6 or 7 gold piles, and randomly change the amount of gold (it will be the same amount in all of them)

<OBJECTS\_GENERATION>

create\_object GOLD {

number\_of\_objects rnd(5,7)

resource\_delta rnd(-200,300)

}

---

##

## Conditionals

Conditionals are pieces of code that will be executed based on whether a specified condition is fulfilled.  The game has predefined most lobby settings as conditions.  Below is the full set of conditions available.

Game modes:

DEATH\_MATCH

REGICIDE

CAPTURE\_THE\_RELIC                (HD/DE only)

CAPTURE\_RELICS                (UP only)

RANDOM\_MAP                (UP/DE only)

TURBO\_RANDOM\_MAP                (UP/DE only) (game mode: random map + the "turbo mode" tickbox)

KING\_OT\_HILL                (UP/DE only) (note that KING\_OF\_THE\_HILL is a [map type](#h.jxjsnahvu5u4), and is always true!)

WONDER\_RACE                (UP/DE only)

DEFEND\_WONDER                (UP/DE only)

EMPIRE\_WARS                (DE only)

BATTLE\_ROYALE                (DE only)

SUDDEN\_DEATH                (DE only)

Map sizes (legacy):  (see also: [Map Sizes](#h.qannz915qgy5) for scaling and dimensions)

TINY\_MAP

SMALL\_MAP

MEDIUM\_MAP

LARGE\_MAP                (Normal - 6 player)

HUGE\_MAP                (Large - 8 player)

GIGANTIC\_MAP

LUDIKRIS\_MAP

Map sizes (modern):  (DE only) (see also: [Map Sizes](#h.qannz915qgy5) for scaling and dimensions)

MAPSIZE\_MINI

MAPSIZE\_TINY

MAPSIZE\_SMALL

MAPSIZE\_MEDIUM

MAPSIZE\_NORMAL

MAPSIZE\_LARGE

MAPSIZE\_HUGE

MAPSIZE\_GIANT

MAPSIZE\_MASSIVE

MAPSIZE\_ENORMOUS

MAPSIZE\_COLOSSAL

MAPSIZE\_INCREDIBLE

MAPSIZE\_MONSTROUS

MAPSIZE\_LUDICROUS

Starting resources:

HIGH\_RESOURCES

MEDIUM\_RESOURCES

LOW\_RESOURCES                (same as default resources)

DEFAULT\_RESOURCES                (same as low resources)

INFINITE\_RESOURCES                (DE only)

RANDOM\_RESOURCES                (DE only)

Starting age:  (DE only)

DARK\_AGE\_START

FEUDAL\_AGE\_START

CASTLE\_AGE\_START

IMPERIAL\_AGE\_START

POST\_IMPERIAL\_AGE\_START

Additional lobby settings:

FIXED\_POSITIONS                (the "team together" tick box)

TURBO\_MODE                (DE only)

TEAM\_POSITIONS                (DE only)

FULL\_TECH\_TREE                (DE only)

AI\_PLAYERS                (DE only) (detect if AI players are present)

SOLID\_FARMS                (DE only) (the "solid farms" tick box in AoE1)

ANTIQUITY\_MODE        (DE only) (the "antiquity mode" checkbox in the lobby)

Player count:  (UP/DE only)

1\_PLAYER\_GAME

2\_PLAYER\_GAME

3\_PLAYER\_GAME

4\_PLAYER\_GAME

5\_PLAYER\_GAME

6\_PLAYER\_GAME

7\_PLAYER\_GAME

8\_PLAYER\_GAME

Team count:  (UP/DE only) (a team is only detected if at least 2 players are on the same team)

0\_TEAM\_GAME

1\_TEAM\_GAME

2\_TEAM\_GAME

3\_TEAM\_GAME

4\_TEAM\_GAME

Team size:  (UP/DE only) (team number refers to lobby order, not the selected team number)

TEAM0\_SIZE0

TEAM0\_SIZE1

TEAM0\_SIZE2

TEAM0\_SIZE3

TEAM0\_SIZE4

TEAM0\_SIZE5

TEAM0\_SIZE6

TEAM0\_SIZE7

TEAM0\_SIZE8

TEAM1\_SIZE0

TEAM1\_SIZE2

TEAM1\_SIZE3

TEAM1\_SIZE4

TEAM1\_SIZE5

TEAM1\_SIZE6

TEAM1\_SIZE7

TEAM1\_SIZE8

TEAM2\_SIZE0

TEAM2\_SIZE2

TEAM2\_SIZE3

TEAM2\_SIZE4

TEAM2\_SIZE5

TEAM2\_SIZE6

TEAM3\_SIZE0

TEAM3\_SIZE2

TEAM3\_SIZE3

TEAM3\_SIZE4

TEAM4\_SIZE0

TEAM4\_SIZE2

Player-in-team:  (UP/DE only) (note that player and team numbers refer to lobby order, not selected number)

PLAYER1\_TEAM0

PLAYER1\_TEAM1

PLAYER1\_TEAM2

PLAYER1\_TEAM3

PLAYER1\_TEAM4

PLAYER2\_TEAM0

PLAYER2\_TEAM1

PLAYER2\_TEAM2

PLAYER2\_TEAM3

PLAYER2\_TEAM4

PLAYER3\_TEAM0

PLAYER3\_TEAM1

PLAYER3\_TEAM2

PLAYER3\_TEAM3

PLAYER3\_TEAM4

PLAYER4\_TEAM0

PLAYER4\_TEAM1

PLAYER4\_TEAM2

PLAYER4\_TEAM3

PLAYER4\_TEAM4

PLAYER5\_TEAM0

PLAYER5\_TEAM1

PLAYER5\_TEAM2

PLAYER5\_TEAM3

PLAYER5\_TEAM4

PLAYER6\_TEAM0

PLAYER6\_TEAM1

PLAYER6\_TEAM2

PLAYER6\_TEAM3

PLAYER6\_TEAM4

PLAYER7\_TEAM0

PLAYER7\_TEAM1

PLAYER7\_TEAM2

PLAYER7\_TEAM3

PLAYER7\_TEAM4

PLAYER8\_TEAM0

PLAYER8\_TEAM1

PLAYER8\_TEAM2

PLAYER8\_TEAM3

PLAYER8\_TEAM4

Game Versions:

UP\_AVAILABLE                (detect UP 1.4+)

UP\_EXTENSION                (detect UP 1.5)

DE\_AVAILABLE                (detect DE)

DE\_GAME\_ROME                (detect DE running Return of Rome, ie. AOE1)

DE\_GAME\_AGE2                (detect DE running regular AoE2)

You can detect other game versions, as well as total conversion mods by exploiting differences in the [predefined constants](#h.9iqqcke3biv) within random\_map.def of the respective game versions.  (See example in the next section).

### if  ConditionLabel  Code

### elseif  ConditionLabel  Code

### else

### endif

Game versions: All

Arguments:

* ConditionLabel - either a [predefined condition](#h.vs551a7tyxet) or a [custom condition](#h.hhofpn9iwfxi)
* Code - anything

Execute a piece of code if a condition is fulfilled, with the option of specifying alternative conditions and pieces of code to execute.

* if is required and will execute the code if the condition is true, and will stop checking further conditions.
* elseif is optional, and will be evaluated if the previous condition(s) were not true.  If true, no further conditions are checked.

* elseif can be specified multiple times.

* else is optional and will be executed if all other conditions fail.
* endif is required to close a conditional

* Can be used within commands or around whole blocks of code.
* Conditionals can be nested.
* BUG (AoC/HD): Comments in dead branches are not ignored.  Do not include any conditional syntax in such comments.  Be especially careful with "if" since it is easy to inadvertently type it in a comment!  For more information, see this external article: [Parser Pitfalls](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42304,,365&sa=D&source=editors&ust=1744981493461122&usg=AOvVaw0XXmPEqpuns_ExopkPu82H)

Example:  Manually scale relic count to map size.

<OBJECTS\_GENERATION>

create\_object RELIC {

min\_distance\_to\_players 25

if TINY\_MAP

number\_of\_objects 5

temp\_min\_distance\_group\_placement 35

elseif SMALL\_MAP

number\_of\_objects 5

temp\_min\_distance\_group\_placement 38

elseif MEDIUM\_MAP

number\_of\_objects 5

temp\_min\_distance\_group\_placement 38

elseif LARGE\_MAP

number\_of\_objects 7

temp\_min\_distance\_group\_placement 48

elseif HUGE\_MAP

number\_of\_objects 8

temp\_min\_distance\_group\_placement 52

else

number\_of\_objects 999

temp\_min\_distance\_group\_placement 52

endif

}

Example2:  Replace the scout with a king when playing regicide.

<OBJECTS\_GENERATION>

if REGICIDE    create\_object KING

else    create\_object SCOUT

endif

{

    set\_place\_for\_every\_player

    min\_distance\_to\_players 7

    max\_distance\_to\_players 9

}

Example3:  Set up a NOT conditional - place a cow when "infinite resources" is not true.

<OBJECTS\_GENERATION>

if INFINITE\_RESOURCES

else

create\_object DLC\_COW {

set\_place\_for\_every\_player

find\_closest

}

endif

Example4:  Check for various game versions.

if DE\_AVAILABLE

elseif DLC\_TIGER /\* present only in HD+DLC and in WK \*/

    if UP\_EXTENSION #define WOLOLOKINGDOMS

    else #define HD\_DLC

    endif

elseif DLC\_COW #define HD\_BASE /\* present in HD base random\_map.def - even though it is a DLC object \*/

elseif UP\_EXTENSION

elseif UP\_AVAILABLE

else #define CONQUERORS\_CD /\* by process of elimination \*/

endif

### #define  ConditionLabel

Game versions: All

Arguments:

* ConditionLabel - text

* AoC/UP - max length is 99 characters
* ANY characters are valid; convention is to use uppercase letters and underscores

Define your own condition labels, to refer to at a later point.

* Do not use any predefined constants.

Example:  Set up seasonal variations for the base terrain.

start\_random

    percent\_chance 20    #define WINTER

    percent\_chance 20    #define AUTUMN

end\_random

<LAND\_GENERATION>

if WINTER    base\_terrain SNOW

elseif    AUTUMN    base\_terrain LEAVES

else    base\_terrain DIRT3

endif

---

##

## Constants

Everything in the game is represented internally by a numeric identifier.  A constant is a label that can be used to refer the random map parser to the right item.  Many useful objects and terrains have predefined constants (see: [Constant Reference](#h.9iqqcke3biv)). However, many objects and terrains also lack a predefined name.  In order to use them in your script, you must first assign a constant to the numeric id.

### #const  Constant  Identifier

Game versions: All

Arguments:

* Constant - text

* AoC/UP - max length is 99 characters
* ANY characters are valid; convention is to use uppercase letters and underscores

* Identifier - number (see: [Constant Reference](#h.9iqqcke3biv))

* Maximum: 16777216 (2^24)

Assign a label of your choice to a numeric ID, to be able to use the terrain/object associated with that ID.

* This is required to use anything that is not predefined.
* Items can have multiple constants assigned to them.
* You cannot re-define a predefined name to a different ID.
* DE: You can use #const as a way to define a number. See [Math Operations](#h.bqp5f3wcm40e). This WILL work:

* #const NUM 10 …. number\_of\_objects NUM

* Pre-DE: You cannot use #const as a way to define a number. This will NOT work:

* #const NUM 10 …. number\_of\_objects NUM

* Constants are interpreted in context (ie. after [create\_object](#h.2vz7nxt2afqo) the game will interpret it as an object, while after [create\_terrain](#h.acnibljecbfg) the game will interpret it as a terrain)

* WARNING: Constants without a proper context are interpreted as syntax.  For more information, see this external article: [Parser Pitfalls](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42304,,365&sa=D&source=editors&ust=1744981493468517&usg=AOvVaw3-SK8u6ubzBZuT5UcMrsSx)

Example:  Define mossy road so you can use it later.

#const ROAD\_FUNGUS 39

Example2:  Define and use variable constants depending on the season.

start\_random

percent\_chance 30 #define WINTER

percent\_chance 30 #define AUTUMN

end\_random

if WINTER

#const LAND\_A 32 /\* snow \*/

#const BERRY\_TYPE 59 /\* berry bush \*/

elseif AUTUMN

#const LAND\_A 5 /\* leaves \*/

#const BERRY\_TYPE 59 /\* berry bush \*/

else

#const LAND\_A 3 /\* dirt 3 \*/

#const BERRY\_TYPE 1059 /\* orange bush \*/

endif

<LAND\_GENERATION>

create\_player\_lands { terrain\_type LAND\_A }

<OBJECTS\_GENERATION>

create\_object BERRY\_TYPE {

number\_of\_objects 5

set\_place\_for\_every\_player

set\_gaia\_object\_only

find\_closest

terrain\_to\_place\_on LAND\_A

}

## Math Operations

Math operations were added to DE in April 2025 and are not available in earlier versions of the game. Numbers can now be saved with [#const](#h.poaiyxi48mi6), and constants will be interpreted as their numeric value when inside a math operation.  Addition, subtraction, multiplication and division can be performed.

* The following operators are available: + - \* /
* Operators require spaces.
* Math must be contained within parentheses.
* Numbers and constants must not have spaces to the bounding parentheses.
* Operations are simply processed left to right.
* Nesting with further parentheses is not possible.
* Rounding occurs after every intermediate operation.
* 0.5 rounds up.
* Pre-defined constants will be interpreted as numbers if inside the parentheses, or if used where numeric inputs are expected.
* Once defined with [#const](#h.poaiyxi48mi6), the constant cannot be re-defined or changed.
* [rnd(min,max)](#h.ml72cdygzrfv) cannot be used inside an operation, but it can be used with [#const](#h.poaiyxi48mi6).
* Math operations can be used almost anywhere a numeric input is accepted.
* Negative numbers can be used.
* Constants above 16777216 (2^24) are not stored accurately.

Example: basic math

<OBJECTS\_GENERATION>

#const A 2

#const B 3

#const RELIC\_COUNT (1 + 2)        /\* 3 \*/

#const GOLD\_COUNT (B \* A)        /\* 6 \*/

#const STONE\_COUNT (GOLD\_COUNT - RELIC\_COUNT \* 2 + 1 / 2) /\* 3.5 -> 4 \*/

#const RAND rnd(1,6)

create\_object RELIC {

        set\_gaia\_object\_only

        number\_of\_objects RELIC\_COUNT

}

create\_object GOLD {

        set\_gaia\_object\_only

        number\_of\_objects (GOLD\_COUNT + (5 + 2)) /\* gives 8 because the (5 is not seen as a number \*/

}

create\_object STONE {

        set\_gaia\_object\_only

        number\_of\_objects (STONE\_COUNT \* 2) /\* gives 8 \*/

}

create\_object FORAGE {

        set\_gaia\_object\_only

        number\_of\_objects (SKIRMISHER - DIRT3) /\* 7-3 = 4 \*/

}

create\_object HOUSE {

        set\_place\_for\_every\_player

        number\_of\_objects (RAND)        /\* parentheses optional here \*/

}

Example: naming actor areas

TODO

Example: automatic scaling

TODO

## Map Sizes

Scaling uses map area, not side length.  Scaling of elevation ([set\_scale\_by\_size](#h.8vbd2ko0sw7f) / [set\_scale\_by\_groups](#h.3vkc0lxd4r4a)), terrains ([set\_scale\_by\_size](#h.g4zvtvsbcm29) / [set\_scale\_by\_groups](#h.cl6w98j0bs9h)), and objects ([set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)) use a 100x100 = 10000 tile reference.  This is smaller than the tiny map size.  Multiply your chosen number by the area ratio listed for a given map size to determine how many tiles/clumps/objects will be generated.

* Note there are some discrepancies regarding the naming of the sizes, particularly regarding normal, large, huge and giant (see table below).
* When scaling to/by map size, the maximum number you should use is 9320, otherwise the scaling will fail on Ludicrous size.
* Map dimensions can be adjusted using [override\_map\_size](#h.sdzu3ermj1ah), in which case any scaling will use the new map area.
* As of March 2024, DE has added additional sizes.  These are accessible in the lobby and scenario editor to players who use the launch option MORE\_MAP\_SIZES

* New rms conditionals have been added for the new sizes as well as all existing sizes to standardize the nomenclature.
* Most maps will need updates if they are to fully function on the new sizes.
* The legacy RMS conditionals continue to work as expected, so there is no need to update maps unless support for the new sizes is desired.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Size (in-game description) | Size (legacy RMS conditional) | Size (modern; with MORE\_MAP\_SIZES) | Dimensions | Area | Area ratio to 100x100 |
| Miniature (1 player) | - | MAPSIZE\_MINI | 80x80 | 6400 | 0.6 |
| Tiny (2 player) | TINY\_MAP | MAPSIZE\_TINY | 120x120 | 14400 | 1.4 |
| Small (3 player) | SMALL\_MAP | MAPSIZE\_SMALL | 144x144 | 20736 | 2.1 |
| Medium (4 player) | MEDIUM\_MAP | MAPSIZE\_MEDIUM | 168x168 | 28224 | 2.8 |
| Normal (6 player) | LARGE\_MAP | MAPSIZE\_NORMAL | 200x200 | 40000 | 4.0 |
| Large (8 player) | HUGE\_MAP | MAPSIZE\_LARGE | 220x220 | 48400 | 4.8 |
| Huge | GIGANTIC\_MAP | MAPSIZE\_HUGE | 240x240 | 57600 | 5.8 |
| Giant | - | MAPSIZE\_GIANT | 252x252 | 63504 | 6.4 |
| Massive | - | MAPSIZE\_MASSIVE | 276x276 | 76176 | 7.6 |
| Enormous | - | MAPSIZE\_ENORMOUS | 300x300 | 90000 | 9.0 |
| Colossal | - | MAPSIZE\_COLOSSAL | 320x320 | 102400 | 10.2 |
| Incredible | - | MAPSIZE\_INCREDIBLE | 360x360 | 129600 | 13.0 |
| Monstrous | - | MAPSIZE\_MONSTROUS | 400x400 | 160000 | 16.0 |
| Ludicrous | LUDIKRIS\_MAP | MAPSIZE\_LUDICROUS | 480x480 | 230400 | 23.0 |

## Walls

* When placing walls with [set\_place\_for\_every\_player](#h.hch89ipgsvb) it is not necessary to specify [number\_of\_objects](#h.btcx5h61er65)
* All that is needed is [min\_distance\_to\_players](#h.asuv2zzhmbsd) and [max\_distance\_to\_players](#h.v2aq68odkdzl) - set both of these to the same value to get square walls.

* Without [max\_distance\_to\_players](#h.v2aq68odkdzl) walls will fail to generate
* If a radius is allowed to vary, the wall will preferentially attempt to link up with forests.
* BUG: If radius varies, the wall may have gaps next to vertical diagonal gates.

* Gates are automatically placed on each segment.
* Make sure to place at least one player object (normally the town center) first before the walls, otherwise the walls will be buggy and centered around the middle of the map.
* Walls do not work properly if the players are completely separated by water.
* Walls may not work properly if everyone is on the same team
* Walls ignore [terrain\_to\_place\_on](#h.t7m0dcvh1px)
* BUG: walls sometimes randomly have gaps when generating in the scenario editor.  This only occurs in the scenario editor.
* The main wall types are:

* PALISADE\_WALL
* WALL, STONE\_WALL
* FORTIFIED\_WALL

* Additional wall types are:

* DLC\_FORTIFIED\_PALISADE\_WALL (500 HP)
* (City Wall - ID 320) (3200 HP)
* (Aqueduct - ID 231) (1600 HP; does not take extra anti-building damage)
* DLC\_FENCE (only 1 HP)
* (Sea Wall - ID 788) (300 HP)

Example: Place a stone wall around players with a radius of 15

create\_object WALL {

        set\_place\_for\_every\_player

        min\_distance\_to\_players 15

        max\_distance\_to\_players 15

}

---

#

# Constant Reference

All constants that are predefined by the game can be found in random\_map.def

You can find that file in the same location as the standard maps.  That would be the gamedata\_x2 folder for DE/HD, and within the gamedata\_x1.drs file for AoC/WK.  random\_map.def is automatically included in all maps, so anything that is defined there can be used in your map, without first having to define it yourself.  It includes most of the common objects and many of the terrains.

Anything not listed there must first be defined with [#const](#h.poaiyxi48mi6) before you can use it.

## Advanced Genie Editor

Advanced Genie editor is a tool used to view and edit the gamedata file and to make data mods.  It is useful for random map scripting, because you can use it to view all the terrains and objects by ID and also look up their properties.

* In DE, you can find it in AoE2DE\Tools\_Builds
* Alternatively, you can also manually [download](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D11002&sa=D&source=editors&ust=1744981493492447&usg=AOvVaw3V-E1w2Wsva43LZ1PBySXr) the most recent version.
* A good external guide to using it can be found [HERE](https://www.google.com/url?q=https://aoe2de.com/mod-development-guide/&sa=D&source=editors&ust=1744981493492744&usg=AOvVaw3nZTdeOg8CpLWOxNKc9C-X)
* And a good overview of the things you can modify [HERE](https://www.google.com/url?q=https://ageofempires.fandom.com/wiki/Genie_Editor&sa=D&source=editors&ust=1744981493492950&usg=AOvVaw23VjtofZK6DoKWNjKuak8m)

![](images/image5.png)

After setting up all your file paths properly, you should be able to load the gamedata file.  The amount of information you get can be overwhelming, so just head over to the Terrains tab or the Units tab.  The main thing that will be useful is the list on the left.  Unfortunately, in DE, the graphics will not be displayed, but in AoC/UP/HD you can see the graphics in a separate window.  Everything that you see listed is a thing that you can potentially use if you define it with [#const](#h.poaiyxi48mi6)

![](images/image12.png)

The Units tab![](images/image4.png)

The Terrains tab

---

##

## Terrains

I have created a spreadsheet detailing all the terrains, their graphics, and their names in the various scenario editors.

[AoE2 Terrains Spreadsheet](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1Fg4BM8dY0FoJ5yoQtL5S4f9LEcMIrYbH0skrFBnrS14/edit?usp%3Dsharing&sa=D&source=editors&ust=1744981493494351&usg=AOvVaw1Gju1vVt2CEL_H7DclMofk)

* If a terrain lacks a predefined constant name, you must define one yourself (with [#const](#h.poaiyxi48mi6)).
* If you want to use non-standard beaches, check out this guide: [Custom Beaches](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42302,,all&sa=D&source=editors&ust=1744981493494752&usg=AOvVaw3SFoqIBYk_EcSYvUmXVD76) or use [beach\_terrain](#h.qlmjwkuqe8hc)
* You can make custom forests by upgrading trees; check out this guide: [creating new forest-types using User-Patch](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/aokcgi/display.cgi?action%3Dct%26f%3D28,44447,,30&sa=D&source=editors&ust=1744981493495083&usg=AOvVaw1xhDrBcMG50jiA61IDKKzd)
* You can generate unused or moddable terrains.  They make great placeholders but are otherwise not useful unless you are making a data mod or total conversion which adds additional terrain graphics.

### Minimap Colors

Terrains use a limited set of colors on the minimap.  They are shown on the spreadsheet.

* Grass terrains and snow terrains (since AoC patch 1.0c) are green.
* Dirt terrains and road terrains are light brown.
* Beach terrains and desert terrains are an even lighter beige.
* Forest terrains are dark green.
* Water terrains are blue, with deeper water being a darker blue.
* Ice terrains are very light blue.
* Farms are an olive color.

Minimap Color Design Theory

In order to design a visually appealing minimap, look carefully at any cosmetic terrain mixing.  Larger clumps of dirt or grass against a backdrop of the other color can look alright, but many small or irregularly-sized clumps may look cluttered and diminish visual clarity on the minimap.

A useful approach on maps featuring [base\_elevation](#h.ppqecxdcopxb) can be to highlight elevated areas and/or slopes with a different color (see Acropolis, Gold Rush, Golden Pit).  Remember that when using [terrain\_mask](#h.e0ug99qovffm) the terrain that is underneath will be the one that provides the properties (including the minimap color) to the final terrain mixture.

## Objects

[Definitive Constants List](https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1llyn7FWKEtmss_WE-6hinMItpsV-h-6qsY8xBlkxUzw/edit%23gid%3D193837369&sa=D&source=editors&ust=1744981493497327&usg=AOvVaw2pIL94hGEYZvx-7w-JSFph) - the spreadsheet may have some typos.  Check out the sub sheets for a list of animals, trees and other resources.

You can also check out this website: [https://halfon.aoe2.se/](https://www.google.com/url?q=https://halfon.aoe2.se/&sa=D&source=editors&ust=1744981493497671&usg=AOvVaw0fKELsqwfH-511qLcZhnVO)

Or use [Advanced Genie Editor](#h.6u6ogmgec4g)

* Note that there are multiple versions of buildings (ie. for each age) - only the default version (the one with the standard predefined constant) will actually be functional (ie. able to train units) in-game.
* Note that in DE, everything with an ID originally in the 900s has been duplicated into the 1300s and you should use the new IDs instead because AIs need the 900s for object class IDs.

## UserPatch Constants

You can find the full list of UserPatch-specific constants in \Reference\Scripting\UserPatchConst.rms within your [UserPatch](https://www.google.com/url?q=http://userpatch.aiscripters.net/guide.html%23&sa=D&source=editors&ust=1744981493498554&usg=AOvVaw2emInbWuIXbWAsweFcKnvu) install directory or [online HERE](https://www.google.com/url?q=http://userpatch.aiscripters.net/upc.rms.txt&sa=D&source=editors&ust=1744981493498687&usg=AOvVaw1d4ODjkhHD1scmNRkC6FuX)

Note that in vanilla UP, these constants must be manually defined (with [#const](#h.poaiyxi48mi6)) before use, but they are predefined in DE (in the random\_map.def file) and WK.

* DE adds additional constants that were not present in UP and also no longer uses some constants that were present in UP.  The lists in the following sections are based on DE.
* HD and CD versions of the game do not natively support any of these (unless running UP).

## Effect Constants

Effect constants are used by [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to modify various things in the gamedata.

* Gaia effects will apply only to gaia, and not to player objects.

* When using [set\_gaia\_civilization](#h.yy69o1bqyfx5), gaia effects will no longer function on objects that can be player-controlled.

SET\_ATTRIBUTE            /\* Type: Attribute Const \*/

ADD\_ATTRIBUTE            /\* Type: Attribute Const \*/

MUL\_ATTRIBUTE            /\* Type: Attribute Const \*/

MOD\_RESOURCE            /\* Type: ATTR\_SET or ATTR\_ADD \*/

MUL\_RESOURCE            /\* Type: ATTR\_DISABLE \*/

SET\_TECH\_COST            /\* Type: ResourceAmount const \*/

ADD\_TECH\_COST            /\* Type: ResourceAmount const \*/

MOD\_TECH\_TIME            /\* Type: ATTR\_SET or ATTR\_ADD \*/

ENABLE\_OBJECT            /\* Type: ATTR\_DISABLE or ATTR\_ENABLE, Value: 0 \*/

UPGRADE\_UNIT            /\* Type: UnitId, Value: 0 \*/

DISABLE\_TECH            /\* Type: ATTR\_DISABLE, Value: TechId \*/

SPAWN\_UNIT                /\* Type: BuildingId, Item: UnitId, Value: 0 \*/

MODIFY\_TECH            /\* Type: ModifyTech const \*/

SET\_PLAYER\_DATA            /\* Type: ATTR\_SET \*/

GAIA\_SET\_ATTRIBUTE

GAIA\_ADD\_ATTRIBUTE

GAIA\_MUL\_ATTRIBUTE

GAIA\_MOD\_RESOURCE

GAIA\_MUL\_RESOURCE

GAIA\_SET\_TECH\_COST

GAIA\_ADD\_TECH\_COST

GAIA\_MOD\_TECH\_TIME

GAIA\_ENABLE\_OBJECT

GAIA\_UPGRADE\_UNIT

GAIA\_DISABLE\_TECH

GAIA\_SPAWN\_UNIT

GAIA\_MODIFY\_TECH

GAIA\_SET\_PLAYER\_DATA

## Effect Type Constants

Attribute constants are used by [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to modify various things in the gamedata.

ATTR\_DISABLE

ATTR\_ENABLE

ATTR\_FORCE

ATTR\_RESEARCH

ATTR\_SET

ATTR\_ADD

## Attribute Constants

Attribute constants are used by [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to modify various object properties in the gamedata.  See this [User Generated Content Guide](https://www.google.com/url?q=https://ugc.aoe2.rocks/general/attributes/attributes/&sa=D&source=editors&ust=1744981493502694&usg=AOvVaw1kTYOq3VF3GS-sWC9LtlmO) or [UP 1.5 Effects & How to use them in Maps](https://www.google.com/url?q=https://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,44466,,30&sa=D&source=editors&ust=1744981493502888&usg=AOvVaw1eMKG3O88PjFC7V_BB1v-W) or check in [Advanced Genie Editor](#h.6u6ogmgec4g) for more details on what these attributes do.

ATTR\_HITPOINTS

ATTR\_LINE\_OF\_SIGHT

ATTR\_GARRISON\_CAPACITY

ATTR\_RADIUS\_1            /\* unit size X \*/

ATTR\_RADIUS\_2            /\* unit size Y \*/

ATTR\_MOVE\_SPEED

ATTR\_ROTATE\_SPEED

ATTR\_ARMOR            /\* armor type\*(65536 or 256) + target value (see A.G.E.) \*/

ATTR\_ATTACK            /\* attack type\*(65536 or 256) + target value (see A.G.E.) \*/

ATTR\_RELOAD\_TIME

ATTR\_ACCURACY\_PERCENT

ATTR\_MAX\_RANGE

ATTR\_WORK\_RATE

ATTR\_RESOURCE\_CARRY            /\* carry capacity \*/

ATTR\_BASE\_ARMOR

ATTR\_PROJECTILE\_ID

ATTR\_UPGRADE\_GRAPHIC            /\* graphics angle \*/

ATTR\_PROJECTILE\_INTELLIGENCE

ATTR\_MIN\_RANGE

ATTR\_STORAGE\_VALUE            /\* population support, tree wood amount, decay time \*/

ATTR\_BLAST\_RADIUS

ATTR\_SEARCH\_RADIUS

ATTR\_HIDDEN\_DAMAGE\_RESIST

ATTR\_ICON\_ID

ATTR\_STORAGE2\_VALUE

ATTR\_STORAGE3\_VALUE

ATTR\_FOG\_FLAG

ATTR\_OCCLUSION\_MODE

ATTR\_GARRISON\_TYPE

ATTR\_RADIUS\_3            /\* unit size Z \*/

ATTR\_CAN\_BE\_BUILT\_ON

ATTR\_FOUNDATION\_TERRAIN

ATTR\_HERO\_STATUS            /\* ADD\_ATTRIBUTE append flags \*/

ATTR\_ATTACK\_DELAY            /\* ADD\_ATTRIBUTE enabled \*/

ATTR\_TRAIN\_LOCATION

ATTR\_TRAIN\_BUTTON

ATTR\_BLAST\_LEVEL

ATTR\_BLAST\_DEFENSE

ATTR\_SHOWN\_ATTACK

ATTR\_SHOWN\_RANGE

ATTR\_SHOWN\_MELEE\_ARMOR

ATTR\_SHOWN\_PIERCE\_ARMOR

ATTR\_NAME\_ID

ATTR\_CREATE\_SDESC\_ID

ATTR\_TERRAIN\_ID

ATTR\_TRAITS            /\* ADD\_ATTRIBUTE append flags \*/

ATTR\_PIECE

ATTR\_DEAD\_ID

ATTR\_HOTKEY\_ID

ATTR\_MAX\_CHARGE

ATTR\_RECHARGE\_RATE

ATTR\_CHARGE\_EVENT

ATTR\_CHARGE\_TYPE

ATTR\_COMBAT\_ABILITY

ATTR\_ATTACK\_DISPERSION

ATTR\_PROJECTILE2\_ID

ATTR\_BLOOD\_ID

ATTR\_HIT\_MODE

ATTR\_VANISH\_MODE

ATTR\_PROJECTILE\_ARC

ATTR\_ATTACK\_GRAPHIC

ATTR\_STANDING\_GRAPHIC

ATTR\_STANDING2\_GRAPHIC

ATTR\_DYING\_GRAPHIC

ATTR\_UNDEAD\_GRAPHIC

ATTR\_WALKING\_GRAPHIC

ATTR\_RUNNING\_GRAPHIC

ATTR\_SPECIAL\_GRAPHIC

ATTR\_OBSTRUCTION\_TYPE

ATTR\_BLOCKAGE\_CLASS

ATTR\_SELECTION\_EFFECT

ATTR\_ATTACK2\_GRAPHIC

ATTR\_RESOURCE\_COST

ATTR\_CREATION\_TIME

ATTR\_GARRISON\_ARROWS

ATTR\_FOOD\_COST

ATTR\_WOOD\_COST

ATTR\_GOLD\_COST

ATTR\_STONE\_COST

ATTR\_MAX\_DUP\_MISSILES

ATTR\_HEALING\_RATE

ATTR\_REGENERATION\_RATE

ATTR\_POPULATION            /\* population cost \*/

ATTR\_MIN\_CONV\_MOD        /\* adds to the minimum time to convert the unit \*/

ATTR\_MAX\_CONV\_MOD        /\* adds to the maximum time to convert the unit \*/

ATTR\_CONV\_CHANCE\_MOD        /\* reduces the chance to convert the unit per conversion roll \*/

ATTR\_FORMATION\_CATEGORY        /\* 0: not using formation, 1: mobile, 2: body, 3: ranged, 4: long ranged, 5: protected \*/

ATTR\_AREA\_DAMAGE                /\* multiplier to the percentage of blast damage the non-directly targeted units receive if positive value, fixed number damage if negative \*/

ATTR\_DAMAGE\_REFLECTION

ATTR\_FRIENDLY\_FIRE\_DAMAGE

ATTR\_REGENERATION\_HP\_PERCENT

ATTR\_BUTTON\_ICON\_ID

ATTR\_SHORT\_TOOLTIP\_ID

ATTR\_EXTENDED\_TOOLTIP\_ID

ATTR\_HOTKEY\_ACTION

ATTR\_CHARGE\_PROJECTILE\_ID

ATTR\_AVAILABLE\_FLAG

ATTR\_DISABLED\_FLAG

ATTR\_ATTACK\_PRIORITY

ATTR\_INVULNERABILITY\_LEVEL

ATTR\_GARRISON\_FIREPOWER

## Resource Constants

Resource constants are used by [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to modify various things in the gamedata.  Those resources that are predefined are listed below.

* Other resources (see [Advanced Genie Editor](#h.6u6ogmgec4g) or the guides listed below) must be manually defined (with [#const](#h.poaiyxi48mi6)) before they can be used.

A full list of available resources can be found in resources\\_common\xs\Constants.xs in your DE game directory, but most will need to be defined as an RMS constant before you can use them.

There are also several attempts to document these resources:

* [User Generated Content Guide](https://www.google.com/url?q=https://ugc.aoe2.rocks/general/resources/resources/&sa=D&source=editors&ust=1744981493510027&usg=AOvVaw0IxXQ-XfUj6NHNc0Ey1hii)
* [AI scripting reference](https://www.google.com/url?q=https://airef.github.io/parameters/parameters-details.html%23ResourceAmount&sa=D&source=editors&ust=1744981493510280&usg=AOvVaw1QrSVO4DRJLla03ji7wsP9)
* [UserPatch Effects Guide](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,44466,0,365&sa=D&source=editors&ust=1744981493510483&usg=AOvVaw1B0uUA2GrWcKeGF0enxI2o)

AMOUNT\_FOOD

AMOUNT\_WOOD

AMOUNT\_STONE

AMOUNT\_GOLD

AMOUNT\_POPULATION\_CAP

AMOUNT\_POPULATION

AMOUNT\_CONVERT\_PRIEST

AMOUNT\_CONVERT\_BUILDING

AMOUNT\_BONUS\_POPULATION\_CAP

AMOUNT\_TOWN\_CENTER\_UNAVAILABLE

AMOUNT\_STARTING\_FOOD

AMOUNT\_STARTING\_WOOD

AMOUNT\_STARTING\_STONE

AMOUNT\_STARTING\_GOLD

AMOUNT\_BUILDING\_TRICKLE\_FOOD

AMOUNT\_BUILDING\_TRICKLE\_WOOD

AMOUNT\_BUILDING\_TRICKLE\_STONE

AMOUNT\_BUILDING\_TRICKLE\_GOLD

AMOUNT\_REVEAL\_ENEMY

AMOUNT\_REVEAL\_RELICS

AMOUNT\_ELEVATION\_HIGHER\_BONUS

AMOUNT\_ELEVATION\_LOWER\_BONUS

AMOUNT\_MONUMENT\_TRICKLE\_FOOD

AMOUNT\_MONUMENT\_TRICKLE\_WOOD

AMOUNT\_MONUMENT\_TRICKLE\_STONE

AMOUNT\_MONUMENT\_TRICKLE\_GOLD

AMOUNT\_FOOD\_GENERATION

AMOUNT\_WOOD\_GENERATION

AMOUNT\_STONE\_GENERATION

AMOUNT\_GOLD\_GENERATION

AMOUNT\_WORKSHOP\_TRICKLE\_FOOD

AMOUNT\_WORKSHOP\_TRICKLE\_WOOD

AMOUNT\_WORKSHOP\_TRICKLE\_STONE

AMOUNT\_WORKSHOP\_TRICKLE\_GOLD

## Technology Constants

Technology constants are used by [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to modify aspects related to technologies.  No technologies have predefined constants, so you must define them first (with [#const](#h.poaiyxi48mi6)) before using them.

* Use [Advanced Genie Editor](#h.6u6ogmgec4g) to view technologies and their IDs.
* You can also check out this website: [https://halfon.aoe2.se/](https://www.google.com/url?q=https://halfon.aoe2.se/&sa=D&source=editors&ust=1744981493513053&usg=AOvVaw0kQsnmEXILbRdx7VvLP7_o)

## ModifyTech Constants

ModifyTech constants are used by [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to modify aspects related to technologies.

ATTR\_SET\_TIME

ATTR\_ADD\_TIME

ATTR\_SET\_FOOD\_COST

ATTR\_SET\_WOOD\_COST

ATTR\_SET\_STONE\_COST

ATTR\_SET\_GOLD\_COST

ATTR\_SET\_LOCATION

ATTR\_SET\_BUTTON

ATTR\_SET\_ICON

ATTR\_SET\_NAME

ATTR\_SET\_DESCRIPTION

ATTR\_SET\_STACKING            /\* allow techs to be researched 256 times! \*/

ATTR\_SET\_STACKING\_RESEARCH\_CAP

ATTR\_SET\_HOTKEY

ATTR\_SET\_STATE

ATTR\_ADD\_FOOD\_COST

ATTR\_ADD\_WOOD\_COST

ATTR\_ADD\_STONE\_COST

ATTR\_ADD\_GOLD\_COST

## Class Constants

Class constants can be used with [guard\_state](#h.7jvxo0vqwqu8), [effect\_amount](#h.1niw1edwqhy5) and [effect percent](#h.7siepjsm3bdc) to target all variations of a unit type, for example all villagers.

There are additional classes which are not predefined.  A list can be found in resources\\_common\xs\Constants.xs in your DE game directory, or by using  [Advanced Genie Editor](#h.6u6ogmgec4g)

Those must be manually defined (with [#const](#h.poaiyxi48mi6)) before they can be used.

VILLAGER\_CLASS

BUILDING\_CLASS

OCEAN\_FISH\_CLASS

SHORE\_FISH\_CLASS

FARM\_CLASS

TREE\_CLASS

TOWER\_CLASS

WALL\_CLASS

GATE\_CLASS

KING\_CLASS

LIVESTOCK\_CLASS

INFANTRY\_CLASS

ARCHERY\_CLASS

ARCHERY\_CANNON\_CLASS

CAVALRY\_CLASS

CAVALRY\_ARCHER\_CLASS

CAVALRY\_CANNON\_CLASS

MONASTERY\_CLASS

SIEGE\_WEAPON\_CLASS

SCORPION\_CLASS

PACKED\_TREBUCHET\_CLASS

UNPACKED\_TREBUCHET\_CLASS

PETARD\_CLASS

WARSHIP\_CLASS

## Miscellaneous Constants

### Map Types

Map type constants are used only for [ai\_info\_map\_type](#h.6o9sfjx8tww0).  If your map is not very similar to a commonly played existing map, it is best to use CUSTOM, or to leave out [ai\_info\_map\_type](#h.6o9sfjx8tww0) entirely.

* Map types are always true when checking for them with [if/](#h.w2egae5vfwo0)[elseif](#h.w2egae5vfwo0) so there is no point in doing so.
* Note that KING\_OF\_THE\_HILL refers to a map type and is always true; for the game-mode [conditional](#h.crt6psej7mdo), use KING\_OT\_HILL instead!
* Non-predefined map types can be seen in this [json file](https://www.google.com/url?q=https://github.com/SiegeEngineers/aoc-reference-data/blob/master/data/datasets/100.json%23L246&sa=D&source=editors&ust=1744981493518217&usg=AOvVaw3j9MtZD00PzGUew91epkOw), although it is untested whether these work and can be recognized by an AI.

ARABIA

ARCHIPELAGO

ARENA

BALTIC

BLACK\_FOREST

COASTAL

CONTINENTAL

CRATER\_LAKE

FORTRESS

GHOST\_LAKE

GOLD\_RUSH

HIGHLAND

ISLANDS

KING\_OF\_THE\_HILL

MEDITERRANEAN

MIGRATION

MONGOLIA

NOMAD

OASIS

RIVERS

SALT\_MARSH

SCANDANAVIA

TEAM\_ISLANDS

YUCATAN

STEPPE

BUDAPEST

VALLEY

ATLANTIC

LAND\_OF\_LAKES

LAND\_NOMAD

CENOTES

GOLDEN\_HILL

MEGARANDOM

MICHI

AMBUSH

CUSTOM

NILE\_DELTA

MOUNTAIN\_PASS

SERENGETI

SOCOTRA

KILIMANJARO

### Cliff Types

Used by [cliff\_type](#h.ydwb5bkkiqmi).

CT\_GRANITE

CT\_DESERT

CT\_SNOW

CT\_MARBLE

CT\_LIMESTONE

### Season Types

Used by [color\_correction](#h.7xt01aajnkw9).

CC\_DEFAULT

CC\_AUTUMN

CC\_WINTER

CC\_JUNGLE

CC\_DESERT

CC\_NIGHT

CC\_EVENING

CC\_SPRING

CC\_SAVANNAH

CC\_ARCTIC

CC\_RAINFOREST

CC\_SWAMP

CC\_STEPPES

CC\_MISTY

CC\_SUMMER

CC\_MURKY

### Assign Types

Used by [assign\_to](#h.b6uul7n11c6g).

AT\_PLAYER

AT\_COLOR

AT\_TEAM

### Player Data Constants

DATA\_CIV\_NAME\_ID

### Civilizations

Used for [set\_gaia\_civilization](#h.yy69o1bqyfx5).  The first number is the ID; the number in brackets is the architecture style.  Image is a screenshot from [Advanced Genie Editor](#h.6u6ogmgec4g).

![](images/image1.png)

---

#

# Scripting and Testing

## Standard Units and Resources

In DE, you will find the object generation contained within the GeneratingObjects.inc file, with map scripts activating specific parts of it.  However, it is much easier to look at land\_resources.inc which is where the AoC objects generation was stored.  That isn't as balanced, but is much more readable.

* For an example of object generation, I have parsed down and simplified GeneratingObjects.inc into a readable format, see: [Simplified Standard Objects Generation](#h.f4cnoa04dy1)

The standard starting units that you should give each player are:

* 1 town center at [max\_distance\_to\_players](#h.v2aq68odkdzl) 0
* Villagers (without specifying how many) at about 6 tiles away (this will automatically adjust for the civilization in AoC/UP/HD, while in DE any extra villagers will be spawned by the town center)
* 1 scout (will automatically be an eagle scout or camel scout when necessary)
* Any [game-mode specific](#h.nlz2m8jsu3b0) objects

The standard (DE) starting resources per player are:

* 1 group of 6 forage bushes at least 10 tiles away
* 1 group of 7 gold mines at least 10 tiles away
* 1 group of 4 gold mines at least 18 tiles away
* 1 group of 4 gold mines at least 21 tiles away
* 1 group of 5 stone mines at least 12 tiles away
* 1 group of 4 stone mines at least 16 tiles away
* 1 group of 4 sheep at around 7 tiles (if cows/water buffalo, use 1 group of 3 instead)

* In tournament  maps, 1 or all of these often start under control of the player.

* 2 groups of 2 sheep at a shared variable min distance (14-24) away (if cows/water buffalo, use 1 group of 3, or 2+1 instead)
* 2 individual boar at least 16 tiles away
* 1 group of either 3 or 4 deer at a variable min distance (14-24) away
* 1 individual predator at least 34 tiles away
* 2 individual trees at 4-5 tiles away
* 3 individual trees at 6-8 tiles away

Notes:

* "at least" means that [find\_closest](#h.kzkb7o2yhtk9) is being used in combination with a minimum distance.
* It is not necessary to conform to the standard starting resources, but they provide a good starting point.

* Indeed, various official maps use different distributions depending on the available space and the nature of the map.

* Sheep/deer/boar can also be their variants (ie. goat/ostrich/elephant for example)
* If distances are randomized, it is best to randomize them in bands, so that no player gets a super far distance compared to other players.

The standard (DE) resources by map size (scattered resources) are:

* 5/5/5/7/8/∞/∞ relics on tiny/small/medium/large/huge/gigantic/ludicrous maps
* Groups of 4 berries on large/huge/gigantic/ludicrous, at least 40 tiles from players (with a very large [temp\_min\_distance\_group\_placement](#h.a5n8aue3ffi4) to ensure low density)
* 2/2/3/3/4/5/26 groups of 3/3/3/3/4/4/4 gold each, on tiny/small/medium/large/huge/gigantic/ludicrous maps, at least 40 tiles from players
* 2/2/3/3/4/∞/∞ groups of 2/2/3/4/4/4/4 stone each, on tiny/small/medium/large/huge/gigantic/ludicrous maps, at least 40 tiles from players
* 2 groups of 1 predator, with [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6) at least 40 tiles from players
* ∞ shore fish, with [temp\_min\_distance\_group\_placement](#h.a5n8aue3ffi4) 6
* 6 fish with [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6) and [min\_distance\_group\_placement](#h.b2u5jna014lf) 4
* ∞ fish of a different type, with [min\_distance\_group\_placement](#h.b2u5jna014lf) 8
* 30 individual trees, with [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)
* 4 birds with [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6)

Notes:

* ∞ means an excess of what will actually fit.
* For scattered resources you can either specify a fixed number for each size, use [set\_scaling\_to\_map\_size](#h.ctsq8l5z99u6) and/or place an excess while specifying a high [temp\_min\_distance\_group\_placement](#h.a5n8aue3ffi4) to restrict the actual count.  All of these approaches can yield similar results.

* For smaller maps and more important resources (ie. relics, gold and stone) the first approach is generally used because it gives the most control.

* On island-style maps, extra resources are instead placed per-player to ensure the same amount on each island.

* For example, on 1v1 tiny islands the relics are 2 for each player and 1 on a central island.

* It is not necessary to conform to the standard starting resources, but they provide a good starting point.

* Indeed, various official maps use different distributions depending on the available space and the nature of the map.

* The exact values are subject to change in future DE updates.

## Simplified Standard Objects Generation

The GeneratingObjects.inc file is used by most of the DE maps to generate objects.  Each map passes various inputs that activate parts of that file.

* For example, #define GNR\_STARTGOLD744CL activates the sections necessary to give the classic 7+4+4 starting gold.

The file is difficult to comprehend and can be especially confusing for newer scripters.  I have therefore parsed out all of the parts that are activated by 2021 Arabia and Coastal, and then merged and simplified those to give the scripts you will find below.  It provides a pretty good overview of how DE handles object generation.  The second one also shows how Empire Wars is implemented.  It is subject to change if the object generation in DE is updated.

* [Simple DE Objects Generation (No Empire Wars)](https://www.google.com/url?q=https://www.dropbox.com/s/r2y3wbp4rrx784c/GeneratingObjectsSimple.inc?dl%3D1&sa=D&source=editors&ust=1744981493531013&usg=AOvVaw2_VIjf2Nw449FhkDT_Xts0) (very simple)
* [Clean DE Objects Generation with Empire Wars](https://www.google.com/url?q=https://www.dropbox.com/s/gozfzrb7n902rpq/GeneratingObjectsCleanWithEW.inc?dl%3D1&sa=D&source=editors&ust=1744981493531318&usg=AOvVaw24swS4bPBZeLft9RCR8o60) (more complicated)
* There is a project on GitHub to make a GeneratingObjects Parser; see [here](https://www.google.com/url?q=https://github.com/gfruleux/AoE2DERMSExtract&sa=D&source=editors&ust=1744981493531562&usg=AOvVaw2zieKgktozbGYXm2MVC75U), [here](https://www.google.com/url?q=https://github.com/gfruleux/AoE2DERMSParser/releases&sa=D&source=editors&ust=1744981493531672&usg=AOvVaw0gV-ahg9LI1m5qhGAnmOu8) and [here](https://www.google.com/url?q=https://github.com/gfruleux/aoe2de_rms_genobj_parser&sa=D&source=editors&ust=1744981493531775&usg=AOvVaw24BlGyoM_xwWt-2oHGkL6y)

## Game Mode Support

The only game-mode that you absolutely must support is regicide, otherwise players will instantly lose because they lack a king.  Nomad will be more streamlined if you follow the advice here.  Death Match and Infinite Resources will be less cluttered if you take the time to remove unnecessary stuff.  Empire Wars is implemented on a per-map basis, so will play out like random map unless you manually code for the units and buildings.

### Regicide

In regicide mode, lacking a King will trigger instant defeat.  Also the starting resources are 500 wood/food, 0 gold, and 150 stone.  Spies is replaced by treason.

It is also possible to use the secondary game mode tick box for regicide instead of the main regicide game mode.  In this case, starting resources are inherited from the chosen game mode and both spies and treason will be available.

* Required: give each player a king.
* Usually a castle and 7 additional villagers are given as well (with the castle providing the housing space for the extra villagers).
* Optional: some maps give players a tower instead of a castle, while nomad maps might not give any buildings.
* Optional: some maps may adjust the starting resources to be standard instead.

### King of the Hill

A monument automatically spawns in the center.  In DE, controlling the monument grants a resource trickle.  This trickle can be modified by using [effect\_amount](#h.1niw1edwqhy5) on the relevant [constants](#h.cym0hd55425r).

### Nomad

Nomad is not actually a game mode.  Nomad is any map where the player starts without a town center and must first build one with their villagers.  If you make a nomad map, you should consider these things:

* Make sure to specify 1 for the isNomad flag for [ai\_info\_map\_type](#h.6o9sfjx8tww0)

* Example: ai\_info\_map\_type CUSTOM 1 0 0
* This may help AIs and will prevent a visibility bug with allied male villagers (fixed in DE)

* Specify [nomad\_resources](#h.fj85jt1i1f2l) to add the cost of a town center (275 Wood, 100 Stone) to every player's starting resources.

* If you do not do this, players will first need to build a lumber camp and gather the necessary wood to afford a town center.

* Do not include a scout or predators, as these would be able to kill villagers very early.
* Consider adding [force\_nomad\_treaty](#h.13why2qs1rix) if you want to prevent villager fighting until everyone has built their town center.

### Death Match

Players start with 20000 wood/food, 10000 gold, 5000 stone.  Typically played in post-imperial.

* Remove berries, sheep, deer, boar, wolves, straggler trees and shore fish, since players will not have time to gather from these resources, and they just get in the way.

### Sudden Death

Players cannot construct new town centers (exception: the first one for nomad starts) and are defeated if they lose their town center.

* Optional: Put some flags or something around the town center to remind people how important it is.

### Infinite Resources (DE only)

This is a resource setting rather than a game mode.  Players will have infinite resources.

* Remove all resources except where required for the visual appeal of the map.
* Do not remove relics, because some civilizations use them for their bonus (ie. Lithuanians).

### Empire Wars (DE only)

Empire Wars is a new game mode in DE.  On Empire Wars, villagers will start harvesting the nearest resource. Huns begin with no houses and extra resources to compensate.  These are the only hardcoded changes.

The goal of Empire Wars is to provide a working feudal age base with an economic population of 28, but you must do so manually.  Check out [Simplified Standard Objects Generation](#h.f4cnoa04dy1) in the Appendix for a consolidated Empire Wars implementation.

The standard Empire Wars start includes the following:

* 1 town center
* 1 scout slightly further away than usual
* A total of 28 villagers distributed across various resources

* On water-heavy maps, some of the villagers may instead be fishing ships

* 2 farms around the town center with 1 villager on each
* 1 mill next to the primary berries
* 4 villagers next to the primary berries
* 1 mining camp next to the primary gold
* 4 villagers next to the primary gold
* 3 lumber camps on the closest forests
* 4/4/4 villagers by the lumber camps
* 1 sheep/cow under the TC
* 6 villagers idle under the TC
* 1 blacksmith
* 6 houses, forming a pseudo-wall
* 1 barracks
* 4 sheep or 3 cows close to the players
* No further sheep/cows and no boar
* No straggler trees around the town center
* Reduced straggler trees on the map in general

### Battle Royale (DE only)

Battle Royale is a new game mode in DE, with several hardcoded changes.  The map gradually constricts, destroying any objects and replacing terrains with a corruption terrain.  Gaia buildings can repeatedly switch control to any player within their line of sight, if the current owner is not within line of sight (includes gaia).  Players always start with zero stone, regardless of the resource level set in the lobby.  Town centers contain a button to pack them into a cart for relocating.

The official Battle Royale maps are custom designed for this game mode.  They use the new trade workshop (ID 1647) to generate resources for players who control them.  A resource trickle (ID 1654) is also given to players, along with a few hero units to start with.  The maps are covered in "camps" - collections of gaia buildings that can be captured.  Powerful camps (especially castles) are guarded by numerous unconvertible (see [set\_gaia\_unconvertible](#h.g4mzdyb4izbo)) gaia units.

* Consider disabling the following units and buildings or including the file BR\_conditions.inc which contains these changes:

<PLAYER\_SETUP>

#const SPIES 408

#const FLEMISH\_REVOLUTION 755

#const FIRST\_CRUSADE 756

#const DONJON\_ENABLER 775

#const TRADE\_COG\_ENABLER 180

#const FISH\_TRAP\_ENABLER 357

effect\_amount DISABLE\_TECH SPIES ATTR\_DISABLE 408

effect\_amount DISABLE\_TECH FLEMISH\_REVOLUTION ATTR\_DISABLE 755

effect\_amount DISABLE\_TECH FIRST\_CRUSADE ATTR\_DISABLE 756

effect\_amount DISABLE\_TECH DONJON\_ENABLER ATTR\_DISABLE 775

effect\_amount DISABLE\_TECH TRADE\_COG\_ENABLER ATTR\_DISABLE 180

effect\_amount DISABLE\_TECH FISH\_TRAP\_ENABLER ATTR\_DISABLE 357

effect\_amount ENABLE\_OBJECT FISHING\_SHIP ATTR\_DISABLE 0

effect\_amount MOD\_RESOURCE AMOUNT\_FOOD\_GENERATION ATTR\_ADD 15

effect\_amount MOD\_RESOURCE AMOUNT\_WOOD\_GENERATION ATTR\_ADD 15

effect\_amount MOD\_RESOURCE AMOUNT\_GOLD\_GENERATION ATTR\_ADD 15

### Antiquity Mode (DE only)

A lobby setting that can be toggled to allow trade to generate wood.  On the official maps it is also used to generate oysters as a water-based gold source.  You can check for the ANTIQUITY\_MODE conditional and generate oysters if it is active.

## AI Support

AIs will be able to play better on maps that are more standard, and which offer plenty of space, and good access to resources.  Very few AIs can effectively migrate bases to new islands or manage fleets across multiple isolated bodies of water.

This guide by AI scripter marathon16 covers more things to consider: [How to make your](https://www.google.com/url?q=https://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42306,,30&sa=D&source=editors&ust=1744981493543390&usg=AOvVaw2SO016Hb4FQTLZSnnuT9z9) [RMS](https://www.google.com/url?q=https://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42306,,30&sa=D&source=editors&ust=1744981493543580&usg=AOvVaw0jJUwxOyDupWOhiaok2ebF)[script more AI-friendly](https://www.google.com/url?q=https://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42306,,30&sa=D&source=editors&ust=1744981493543703&usg=AOvVaw1oJ6NG8kY9mVTOZDWEAJqD)

* Note that portions of the AI scripting community is (still) on UP/WK, not on DE.

## Testing

### Scenario Editor

You can generate maps in the scenario editor (UP/HD/DE).  Custom maps are shown in the map list.  You do not need to restart the game; just save changes to your script and hit "generate map" to observe the changes.  You can specify a specific seed to debug said seed or to observe the exact effect of changing some part of your script.  The usual process of random map scripting involves having both the map script and the scenario editor open, and repeatedly generating your script as you work on it.

* By default, players will be unteamed in the scenario editor, but if you set up teams in the diplomacy tab, you can test team maps (UP/DE only)
* You can test the object generation for other game modes such as [Empire Wars](https://www.google.com/url?q=https://www.ageofempires.com/games/aoeiide/empire-wars/&sa=D&source=editors&ust=1744981493545079&usg=AOvVaw3rj3d7E8t-yv1QL40wk-47) by selecting secondary game modes from the victory tab.

Testing in the scenario editor has some limitations and bugs:

* [set\_gaia\_civilization](#h.yy69o1bqyfx5) [resource\_delta](#h.ndaw6icg9cnp) [set\_gaia\_unconvertible](#h.g4mzdyb4izbo) all do not work when testing from the editor.  This also applies to many things you might change with [effect\_amount](#h.1niw1edwqhy5) and [effect\_percent](#h.7siepjsm3bdc).
* Bug: Walls may sometimes have gaps in them or fail to generate entirely.  This is a legacy issue exclusive to the scenario editor, so don't be worried if you see gaps.
* BUG (DE): Water animation persists across repeated generations.  Disable animated water in the options to avoid this visual distraction.  This issue is exclusive to the scenario editor, so don't be worried.

### Single Player

Alternatively, you can test in single-player.  This may be necessary for testing specific game modes and/or lobby settings.  It may be beneficial to set visibility to "All Visible" or to use the marco and polo cheats.

* When in game, you can bring up the menu and hit "restart" - this will regenerate the map from the same seed, but will use any changes to your script that you have saved.  If you want to test a different seed, you need to start a new match.

### Debugging Tips

* You do not need to reboot AoE2 to see changes in your map script.  Simply save changes in the file and generate the map again.
* Both the scenario editor and single player offer the opportunity to repeatedly generate using the same map seed and then make changes until a particular buggy generation no longer occurs.
* An incomplete [comment](#h.2knaho4i0qpg) (one that opens but doesn't close) can quickly be used to disable large parts of your script.
* [Random code](#h.87mv66lnefdm) may influence other bits of random code in unrelated areas when using the same seed; ie. commenting out a random block at the end of your script may change which random branch is chosen at a different (earlier) point in your script.
* Generating a large excess with [number\_of\_objects](#h.btcx5h61er65) can be used to visualize all possible spawn locations for that object.
* Using [height\_limits](#h.oezholffksgg) with terrain of a different [minimap color](#h.1mrucebr642p) can help visualize on the minimap where [elevation](#h.szmawgkuqtsf) is being generated.
* [default\_terrain\_replacement](#h.p16vd5cszmhm) can be used to visualize which paths [connections](#h.urxh5ze1aaoh) are taking.
* You can view the map in [CaptureAge](#h.24lmsw81mk8g) while testing from the scenario editor or single player.
* Adding EDITOR to the launch options will launch the game directly into the scenario editor (DE only)

## Loading Times

The actual parser is not particularly fast and it will still go through everything in the file, including comments and logical branches that are not chosen.  Maps that are over 1 MB in file size will take several seconds to parse, during which the game will appear to stop responding.

* This is not a concern for most maps.  Only extremely large maps such as MegaRandom (380 KB) or [Dire Straits](https://www.google.com/url?q=https://docs.google.com/document/d/1E_Si9iXmzUqFuptkW-8F6XdmoxDXNUG36XIhnh86krU/edit&sa=D&source=editors&ust=1744981493549516&usg=AOvVaw04tlKFvRRY0otkktJYSYZG) (1700 KB) cause any noticeable delay.
* If your map is considerably smaller, but still very slow to load, it may be due to having many actor areas or computationally difficult connection generation.  Also keep in mind that the first time any textures and sprites are loaded into memory takes (significantly) longer than subsequent generations (noticeable only on DE, where the textures and sprites are larger).
* Lobby transfer time is perhaps the most significant consideration.  Files over 1 MB in file size may take over a min to transfer to other players in the lobby (tested in DE).

## Publishing a Map

If you are just making a map for friends, you just could send them the file and have them manually place it in their game directory.  For any other cases, it makes sense to upload your map as a mod.

### Definitive Edition

DE does not use the Steam Workshop.  You will need a Microsoft account.  If you don't have an account, create one on [https://account.microsoft.com/](https://www.google.com/url?q=https://account.microsoft.com/&sa=D&source=editors&ust=1744981493550926&usg=AOvVaw3SWLrfUS9IvF8OZ1nc4TtB)

You can browse mods at [https://www.ageofempires.com/mods/](https://www.google.com/url?q=https://www.ageofempires.com/mods/&sa=D&source=editors&ust=1744981493551134&usg=AOvVaw2ic_XMbSMTO10fWXILOM-0)

However, subscribing in your browser downloads nothing.  To actually get a mod, you must subscribe to it in-game using the mod manager.

You can also use [https://mods.aoe2.se/](https://www.google.com/url?q=https://mods.aoe2.se/&sa=D&source=editors&ust=1744981493551499&usg=AOvVaw0ud55EboWcYvIp1ghoVmLp) to browse and download mods without using the official site.

To publish your own map as a mod using the in-game mod manager:

* Navigate to C:\Users\<username>\Games\Age of Empires 2 DE\<numericID>\mods\local
* There create a folder with the name of the your mod
* Then create sub-folders to mirror the main game directory
* The final result should look like this:

C:\Users\Zetnus\Games\Age of Empires 2 DE\76561198019184368\mods\local\Zetnus HyperRandom\resources\\_common\random-map-scripts

* Put your map(s) in that random-map-scripts folder
* Sign in to your Microsoft account by clicking on your name in the main menu
* In game, navigate to the "My mods" tab, within "Mods"
* Click on "Publish Mod"
* Choose a title and make sure the correct folder is selected
* Choose an image (it must be a png or jpg)
* Add a description.  If the text turns red, that means DE's incompetent chat filter doesn't like something you wrote.  You can either try and fix it, or just leave the description blank for now.
* You cannot edit changelongs later, so double check your spelling there!
* Hit "Publish Now"
* Once it is uploaded, a web browser window will open showing your mod.
* Edit the description using on the website and re-add all the profane obscenities that the chat filter didn't like, and/or to add more images.

To update your mod:

* Place the new files in the relevant folder (in mods\local)
* Navigate to "My Mods" in-game
* Click on "Update Mod"
* Follow the steps as above.
* Updates should be pushed out to players automatically (when they restart the game?)

To publish your own map as a mod using the website:

* Follow the same steps as above, but do not start the game.
* Instead, click on your mod folder and and choose "send to compressed (zipped) folder"
* Check the contents of your zip; if you see a folder with the same name as your zip, this will NOT work.  Move the contents of that part up one level.

Wrong ✘: Zetnus HyperRandom.zip\Zetnus HyperRandom\resources\\_common\random-map-scripts

Correct ✔: Zetnus HyperRandom.zip\resources\\_common\random-map-scripts

* Upload your mod to [https://www.ageofempires.com/mods/create/](https://www.google.com/url?q=https://www.ageofempires.com/mods/create/&sa=D&source=editors&ust=1744981493556435&usg=AOvVaw2IV_HhTfrXsIbkiEUMH7gU)
* To update your mod using the website, follow exactly the same steps except that you will need to go to [https://www.ageofempires.com/mods/mine/](https://www.google.com/url?q=https://www.ageofempires.com/mods/mine/&sa=D&source=editors&ust=1744981493556877&usg=AOvVaw2d58E7rzUF28SkHpfwn7kK) and choose the relevant mod and click on "edit"

### HD Edition (2013)

The HD Edition uses the Steam Workshop.  The process is fundamentally similar to using the in-game mod manager in DE.  Follow this guide:

[How to Publish/Update Workshop Items](https://www.google.com/url?q=https://steamcommunity.com/workshop/discussions/18446744073709551615/864979883911637197/?appid%3D221380&sa=D&source=editors&ust=1744981493557711&usg=AOvVaw0iA6X_WmJCXyaNQB8olg5x)

### Voobly

[Step-by-step guide for uploading a mod](https://www.google.com/url?q=https://www.voobly.com/pages/view/uploadmod&sa=D&source=editors&ust=1744981493558110&usg=AOvVaw2D4uzaPLcd1LHE4SQLEFit)

[Game Mod Guide](https://www.google.com/url?q=https://www.voobly.com/pages/view/gamemods&sa=D&source=editors&ust=1744981493558328&usg=AOvVaw0juJLh7tertRBOJbelHcwc)

### AoE2map

[https://aoe2map.net/](https://www.google.com/url?q=https://aoe2map.net/&sa=D&source=editors&ust=1744981493558519&usg=AOvVaw0JbuvwpaAhPWY7VHxaZJCH)

This is an external site that has been used by the RMS community to upload map scripts, in the pre-DE era.  Just make an account, everything is very self-explanatory.

### Age of Kings Heaven

[Age of Kings Heaven - The Blacksmith :: Random Maps](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/lister.php?category%3Drandom&sa=D&source=editors&ust=1744981493558943&usg=AOvVaw33F5ZphvCPLOnraaNuRxvI)

This is a very old site, where you can find a trove of older map scripts.  You'll need to register an account before you can upload to the blacksmith.  Note that the file size limit for screenshots is very low (by modern standards).  Also note that the blacksmith is curated - this means that any uploads will need to be approved by staff before they are visible.  This may take up to 1-2 weeks if people are busy.  So be patient.

### Full Map Screenshots![](images/image8.png)

In the CD version of the game (including UP and WK), you can take a screenshot of the entire map, using CTRL+F12

This was broken with the new rendering engine in HD, and has not been reimplemented for DE.  However, DE officially supports [CaptureAge](#h.24lmsw81mk8g), which is your best option to take full map screenshots in DE.

Alternatively, there are several implementations that attempt to mimic the behavior, but they rely on using an external program to take a bunch of screenshots and then stitch them together.  See external guide: [AoE2 DE Full-Map Screenshot Guide](https://www.google.com/url?q=https://docs.google.com/document/d/e/2PACX-1vQWGL0UYvF5cn7L6bR72J57oj8n6TqY5hVThD9WfECUnLsNZSvhBLUB1LDoJ4pXXOIVsTs5kDVnTrmW/pub&sa=D&source=editors&ust=1744981493560310&usg=AOvVaw3eAOZMgx_iF9IxlCDU2zRd) and this site: [AoE Full Map Capture by](https://www.google.com/url?q=https://coltenney.itch.io/aoe-full-map-capture&sa=D&source=editors&ust=1744981493560445&usg=AOvVaw1FnDMLUSdhHa7eWHLDsnMI) [coltenney](https://www.google.com/url?q=https://coltenney.itch.io/aoe-full-map-capture&sa=D&source=editors&ust=1744981493560529&usg=AOvVaw3mUiK7IE9SYTlHBrISDhkh)

If your map is backwards-compatible, you can take screenshots in UP or WK.  But if you have used a lot of new terrains/objects/features, it may not be worth the effort to make it backwards-compatible.

You can always just screenshot the minimap too.

### CaptureAge![](images/image9.png)

[CaptureAge · Home](https://www.google.com/url?q=https://captureage.com/&sa=D&source=editors&ust=1744981493561052&usg=AOvVaw3L7qo0dPA2eLnWghh_24Iy)

CaptureAge is a casting program for Age of Empires.  It was originally developed for use on Voobly.  The basic DE version is available to the public for free.  CaptureAge allows for zooming out all the way, and you can then use a snipping tool to take a screenshot of the whole map.

* Capture Age can be launched when using "test" from the scenario editor, or when playing a game with cheats enabled. Alternatively, Capture Age can be used to view recorded games.
* The shortcut ALT+o can be used to hide the user interface and move the minimap to the corner or to hide it entirely.

### Map Icons

![](images/image11.png)

Map icons are the images that appear on the map selection screen in DE.

* Take a look at resources\\_common\wpfg\resources\mapicons or widgetui\textures\menu\mapicons for reference.
* The game will rescale your image into an appropriately-sized square.  The corners should be transparent.
* The simple way is to provide a .png file of the same name as your map script, in the same folder as your map script.  No .json file needed.
* Map icons require restarting the game to appear after enabling a map mod.

It is also possible to make a .json file of the same name as one of your maps, and then reference the image(s), which can be in a different folder, or be a different file format.

* Example .json file:

{

        "custommaps" : [{

                "name" : "Green Arabia",

                "iconRef" : "IconGreenArabia"

        }],

        "UserMaterials": [{

                    "Material": "IconGreenArabia",

                    "FileName": "Green Arabia.dds"

        }]

}

[Map Icons Made Easy (video)](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DADL2EMBdhzk&sa=D&source=editors&ust=1744981493563650&usg=AOvVaw3jfbjkYS0bguh7Vp-3y2TG) 20 min video covering everything you might want to know about making map icons

## Updating an Old Map for DE

Theoretically, an old map script should run on DE without having to change anything, however there are a few things to look out for.

### Elevation Scaling

There was a legacy bug where [set\_scale\_by\_size](#h.8vbd2ko0sw7f) and [set\_scale\_by\_groups](#h.3vkc0lxd4r4a) for elevation had their behavior inverted.  This bug has been fixed in DE.  Additionally, it was not previously known that [set\_scale\_by\_size](#h.8vbd2ko0sw7f) and [set\_scale\_by\_groups](#h.3vkc0lxd4r4a) are mutually exclusive, since the standard maps usually use both attributes.  As a result, elevation scaling will behave differently in DE than it would have pre-DE.  A map can be made compatible with both DE and pre-DE by using a simple conditional, or if you only need your map to run on DE, all you need to do is swap the attributes.

Example: adjust elevation scaling according to game version.

if DE\_AVAILABLE        set\_scale\_by\_size

else        set\_scale\_by\_groups        /\* this is bugged and and actually scales by size in pre-DE \*/

endif

### Base Terrain Default

[base\_terrain (terrain)](#h.ptxp1ht2fh0p) was changed in DE such that it no longer uses grass as the default if no base terrain is specified.  Some legacy maps will be missing forests and need to be updated by adding the following to any affected create\_terrain commands:
base\_terrain GRASS

### Additive Connections

In DE connections act on the terrain that existed before connection generation, and connections cannot replace each other by default.  To use the legacy (pre-DE) behavior where connections can replace each other, activate [accumulate\_connections](#h.bd2l5930vfzf)

This only matters if you have multiple connections being generated sequentially (which is uncommon).

### UserPatch Effects

Most UserPatch effects are supported in DE, as of January 2021.  However, [terrain\_state](#h.tdph3oglggjk) and [weather\_type](#h.ht15fzasksgc) are not implemented in DE.  Weather is cosmetic only and can be modified in DE using [color\_correction](#h.7xt01aajnkw9), while terrain restrictions can be modified with [effect\_amount](#h.1niw1edwqhy5).  Neither feature was commonly used in UP map scripts.

A few UP effects may function differently in DE, so double check to make sure everything works as expected.  Specifically look at any units with modified attack or armor values.

Also some effects have been depreciated or replaced such as ENABLE\_TECH.

### WololoKingdoms Terrains

If your map was made for WK and defines terrains using [#const](#h.poaiyxi48mi6), you will need to redo these definitions, since WK moved various terrain IDs when compared to AoC/HD/DE. See [Special Note for WololoKingdoms](#h.al63pivw8b4c)

### Minor Stuff

* [min\_distance\_to\_players](#h.asuv2zzhmbsd) no longer applies to ALL lands anymore.

* This bug was fully fixed, and then partially reverted, so it may change again.

* Certain unused objects in the gamedata lack graphics in DE (such as the beta berserk)
* All object IDs in the 900s have been duplicated into the 1300s because the 900s are also used for object class IDs.  Use the new IDs for the relevant objects (most notably the elephant).

* Only matters if you are manually defining using [#const](#h.poaiyxi48mi6)

* [base\_elevation](#h.ppqecxdcopxb) cannot be used for water lands (unlike in UP, where it can)
* Beach terrains are no longer restricted terrains for placing boars, but still for deer.  Terrain restrictions can be modified with [effect\_amount](#h.1niw1edwqhy5)
* [comments](#h.2knaho4i0qpg) in dead logical branches are now properly ignored, so if your map was relying on a buggy comment, you will need to fix that.

### New Things to Consider Adding

* [enable\_balanced\_elevation](#h.izx21xcrwjlg) in every [create\_elevation](#h.h85o0pyielaj) command
* [set\_circular\_placement](#h.15fez3e52vqr) for all player objects unless using a walled (square) start
* [avoid\_forest\_zone](#h.ym7v1j9vbnle) and [avoid\_cliff\_zone](#h.t2916w9l2cff) to prevent stuck resources
* [terrain\_mask](#h.e0ug99qovffm) when doing cosmetic terrain mixing (because it looks nice)
* [color\_correction](#h.7xt01aajnkw9) (instead of [weather\_type](#h.ht15fzasksgc) from UP)
* [force\_nomad\_treaty](#h.13why2qs1rix) on nomad maps
* [behavior\_version](#h.seeuqpcozayb) to use the new land generation behavior (make sure to adjust the land sizes accordingly)
* Adding a custom distance to [set\_avoid\_player\_start\_areas](#h.ijxhxwahit2u) if you want forests to stay further from players
* [Empire Wars](#h.xzwndngyca0k) support
* [override\_map\_size](#h.sdzu3ermj1ah) on water maps to make them slightly larger
* support for the additional [map sizes](#h.qannz915qgy5)

---

#

# Links and Resources

## Videos

TheMadCADer has a bunch of videos that are well worth watching; here is a link to the [playlist](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DFk9Sc6YqHFw%26list%3DPLYYZYNnmocy0XrBC1m1xj1__xRoOri8G5&sa=D&source=editors&ust=1744981493570637&usg=AOvVaw02fEDm60u_qC-kQCgtYkoW)

## Official Documentation

* [DE RMS Feature Documentation](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/rms-features&sa=D&source=editors&ust=1744981493570935&usg=AOvVaw2bIfyYYrV0SEd8jFY0uZDe) by Forgotten Empires; but has screenshots and examples, but does not include more recent additions.
* [.xs scripting in Age of Empires II: Definitive Edition](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/xs-scripting-in-age-of-empires-ii-definitive-edition&sa=D&source=editors&ust=1744981493571243&usg=AOvVaw3fvhKfMoi2bYv8jMSLkdCk) by Forgotten Empires, but probably does not include more recent additions.
* [UserPatch Scripting Reference](https://www.google.com/url?q=http://userpatch.aiscripters.net/reference.html%23&sa=D&source=editors&ust=1744981493571514&usg=AOvVaw3I3A6VESNbmU0lyFAuLCyG) and [RMS #Const Updates](https://www.google.com/url?q=http://userpatch.aiscripters.net/&sa=D&source=editors&ust=1744981493571647&usg=AOvVaw3RDpajjiT5gQ88jc_A7QgK) - both very useful for anything added by UP
* [AgeII HD Script Reference](https://www.google.com/url?q=https://steamcommunity.com/workshop/discussions/-1/2217311444333302935/?appid%3D221380&sa=D&source=editors&ust=1744981493571897&usg=AOvVaw3CKnjPvfGNOoUDW42c0dDz) official, but has some typos (and is ultimately just a copy of the UP reference)
* [Random Map Scripting Guide (RMSG)](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D11773&sa=D&source=editors&ust=1744981493572227&usg=AOvVaw1Q3eJIquMXZ2CYVyczBq8Z) by Ensemble Studios (the same one you can find in your game directory).  (outdated)

## General Guides

* [AoE2DE UGC Guide](https://www.google.com/url?q=https://ugc.aoe2.rocks/&sa=D&source=editors&ust=1744981493572536&usg=AOvVaw3eFvcak30VxG-m6c5U1LOP) has guides on xs scripting, scenario triggers, and game data attributes
* [AOE2 Random Map Scripting Part 1 – The Basics](https://www.google.com/url?q=https://twharris.dev/2021/04/11/aoe2-random-map-scripting-part-1-the-basics/&sa=D&source=editors&ust=1744981493572808&usg=AOvVaw1x7hbBqvhf9QcMBdlsiVwF) by Thomas Harris
* [AOE2 Random Map Scripting Part 2 – Arabia](https://www.google.com/url?q=https://twharris.dev/2021/05/02/aoe2-random-map-scripting-part-2-arabia/&sa=D&source=editors&ust=1744981493573005&usg=AOvVaw03DVrrdI6Op-wPZ5mTyG_8) by Thomas Harris
* [UP 1.5 Effects & How to use them in Maps](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/aokcgi/display.cgi?action%3Dct%26f%3D4,44466,,30&sa=D&source=editors&ust=1744981493573215&usg=AOvVaw2OLLuFSY4LuN82LRqNQ6xi) helps to understand the capabilities of UP
* [XS Scripting For Beginners](https://www.google.com/url?q=https://divy1211.github.io/AoE2DE_UGC_Guide/general/xs/beginner/&sa=D&source=editors&ust=1744981493573465&usg=AOvVaw1YCkAIwkicQPM_uim7zUu6) everything you need to know about XS scripting
* [Random Map Syntax](https://www.google.com/url?q=https://hungarian-notation.github.io/rms-toolkit/rms.xml%23objects-create_object&sa=D&source=editors&ust=1744981493573685&usg=AOvVaw1nSjW26cgKvlQ2GyYbrYWK) very concise, but not fully up-to-date
* [A Guide for Creating Maps](https://www.google.com/url?q=https://docs.google.com/document/d/1zzF-qYDnsW5s0vDsZ1bGpI55C5JefYldXQEfQaKFxU4/edit&sa=D&source=editors&ust=1744981493573938&usg=AOvVaw0DkMtewexvQp_7iLCGkpC8) by HenkDeSuperNerd; unfinished, but goes into good detail
* [Random Map Scripting Links and FAQ](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dst%26fn%3D28%26tn%3D42485%26st%3Drecent%26f%3D28,42485,0,365&sa=D&source=editors&ust=1744981493574187&usg=AOvVaw25xv0AEugZyndESYmxk4cm) forum thread that is also a precursor to this guide
* [Alchemy-AOE-Published-Specifications](https://www.google.com/url?q=https://github.com/Alchemy-AOE-Community/CHEM-Published-Specifications/tree/download-to-click-links/STANDARD&sa=D&source=editors&ust=1744981493574433&usg=AOvVaw2V6VjtUBQKK2waeGJHCV8r) an attempt to codify the specifications for what constitutes a competitive map.

## Specific Guides

* [MadLands Utility](https://www.google.com/url?q=https://www.aoezone.net/threads/madlands-utility-for-rms.166398/&sa=D&source=editors&ust=1744981493574742&usg=AOvVaw1enfffpAArAe94zxPVNEe5) generate a bunch of fixed land positions using Excel, and also manage map packs more easily
* [Error-Handling with actor areas](https://www.google.com/url?q=https://docs.google.com/document/d/1rShRudnsaqU8vgNuyhjSnFvLQq_K0eAF9Ftdl2KnY-o/edit&sa=D&source=editors&ust=1744981493575019&usg=AOvVaw3NjpZSIdROuP1qB-bdo6s5) debugging map generations using actor areas
* [Dire Straits & creating random RM maps](https://www.google.com/url?q=https://docs.google.com/document/d/1E_Si9iXmzUqFuptkW-8F6XdmoxDXNUG36XIhnh86krU/edit&sa=D&source=editors&ust=1744981493575254&usg=AOvVaw068h_eYg0gAKxozwKm4Cvq) an exercise in precomputing maps
* [Parser Pitfalls](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42304,,all&sa=D&source=editors&ust=1744981493575451&usg=AOvVaw1R7kKbxrxisxB02ZoBiAEl) keep the RMS parser from misbehaving
* [Land generation in Age of Empires II](https://www.google.com/url?q=https://www.dropbox.com/scl/fi/gmk0lmwsknu8mlssgd2mb/LandStyles_explained_jan19.docx?rlkey%3Dpbizy742b6xi5vldxzfx17mkb%26dl%3D1&sa=D&source=editors&ust=1744981493575701&usg=AOvVaw35YGZS1sMsgpBnOtH_ig2t) a detailed look at land generation
* [creating new forest-types using User-Patch](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/aokcgi/display.cgi?action%3Dct%26f%3D28,44447,,30&sa=D&source=editors&ust=1744981493575912&usg=AOvVaw1Cja6H3JSMdVlgZSgCcfzh) upgrade forests with UP
* [All About Cliffs](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42261,,30&sa=D&source=editors&ust=1744981493576114&usg=AOvVaw0ngjGvb41Xxw0S89eQdUlb) more than you ever wanted to know about cliffs
* [Custom Beaches](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42302,0,all&sa=D&source=editors&ust=1744981493576317&usg=AOvVaw0iyNhhi5MtVm3T1XXrbkF4) use the new beach terrains in your map
* [Weather Effects with UserPatch 1.5](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42296,,all&sa=D&source=editors&ust=1744981493576534&usg=AOvVaw1JnlUvV9b_XKbKeKlb_xjA)
* [Unequal Player Starts](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D26,42259,0,all&sa=D&source=editors&ust=1744981493576709&usg=AOvVaw3aofb7R4jJQB6sTDWwb1G4) and [Unequal Player Starts - part 2](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dst%26fn%3D26%26tn%3D42283%26st%3Drecent%26f%3D26,42283,0,0&sa=D&source=editors&ust=1744981493576867&usg=AOvVaw00fOUK839S-dvT0Ojw9bsh) create asymmetric starts
* [Random Map Advanced Skills](https://www.google.com/url?q=http://www.hawkaoe.net/bbs/forum.php?mod%3Dviewthread%26tid%3D139741&sa=D&source=editors&ust=1744981493577066&usg=AOvVaw1u8CUEc7sPITpR8ddAzJGN) (in Chinese)
* [AoE2Map Snippets](https://www.google.com/url?q=https://snippets.aoe2map.net/&sa=D&source=editors&ust=1744981493577215&usg=AOvVaw2doQob9eQL-ZT6X6T4RkPw) a collection of useful bits of code (many for UP effects)
* [Modifying Starting Resources](https://www.google.com/url?q=https://www.aoezone.net/threads/random-map-scripting-regicide-inconsistency-adjusting-starting-resources-enabling-custom-gamemode-selection-and-more.144894/&sa=D&source=editors&ust=1744981493577478&usg=AOvVaw2O8YVdOogMxqa34_XsiiEW) (specifically for custom UP regicide)
* [Everything is Regicide with with UserPatch 1.5](https://www.google.com/url?q=https://hszemi.de/2017/09/everything-is-regicide-with-userpatch-1-5/&sa=D&source=editors&ust=1744981493577682&usg=AOvVaw11ifox7ec5rtRWha3FrQ8t) combine regicide with other game modes
* [https://eso-community.net/viewtopic.php?p=436182](https://www.google.com/url?q=https://eso-community.net/viewtopic.php?p%3D436182&sa=D&source=editors&ust=1744981493577885&usg=AOvVaw3GvsnZ73Aqera8GPqnHnnr) XS scripting
* [https://aok.heavengames.com/cgi-bin/forums/display.cgi?action=ct&f=4,44731,,30](https://www.google.com/url?q=https://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,44731,,30&sa=D&source=editors&ust=1744981493578119&usg=AOvVaw39fCMJP-ekuAWY00CxxD5r) XS scripting
* [https://www.hawkaoe.net/bbs/thread-147206-1-1.html](https://www.google.com/url?q=https://www.hawkaoe.net/bbs/thread-147206-1-1.html&sa=D&source=editors&ust=1744981493578312&usg=AOvVaw2bWZlWUUh2zOJFa5pmJ73E) XS scripting

## Example Scripts

You can also open up any existing map script and take a look.  A lot can be learned by modifying an existing map and observing the effects of your changes.

* The original [Random Map Scripting Guide (RMSG)](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D11773&sa=D&source=editors&ust=1744981493578811&usg=AOvVaw0t8AYLFoLluScOUBac6xQs) by Ensemble Studios (the same one you can find in your game directory) contains a commented version of Coastal.
* The classic AoC versions of the official maps can be found in [this mod](https://www.google.com/url?q=https://www.ageofempires.com/mods/details/21859/&sa=D&source=editors&ust=1744981493579162&usg=AOvVaw0SaSXjie68dJT5HHF0Zf3G), and are much more simple to read than the new DE versions of the official maps.  Do NOT start out with modern tournament versions of maps, (especially not from Arabia or any of the Red Bull Wololo maps).
* The ES\_ maps are also good choices to look at.  They are found in your random-map-scripts folder.
* In the Appendix you will find [Simplified Standard Objects Generation](#h.f4cnoa04dy1) with a parsed down version of the DE objects generation.
* In Reference\Scripting\Examples within your UserPatch install directory, there are three scripts to showcase the functionality of Userpatch 1.5

## Syntax Highlighting

Getting an RMS syntax highlighter for your text editor of choice will help you spot typos and generally improve the scripting experience.  The community has syntax highlighters for numerous text editors.

### Notepad++

* [By Zetnus](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D13247&sa=D&source=editors&ust=1744981493580571&usg=AOvVaw0v4d7MEk09F2UM_dJw_J3j) up-to-date for DE

### VIsual Studio Code

* [By Anda](https://www.google.com/url?q=https://marketplace.visualstudio.com/items?itemName%3Danda.rms-check-vscode&sa=D&source=editors&ust=1744981493580808&usg=AOvVaw3U24v02wE8lwsp86CJL7A2) which is not only highlighter, but also a linter - meaning it can be used to check your script for bugs or compatibility issues. Mostly up-to-date for DE.
* [AoE XS Scripting](https://www.google.com/url?q=https://marketplace.visualstudio.com/items?itemName%3DDivy.vscode-xs&sa=D&source=editors&ust=1744981493581123&usg=AOvVaw0FFEo7kNW7XTN5WhLcjSfx) for xs scripting - not directly for RMS scripting

### Sublime Text

* [By Nikita Litvin](https://www.google.com/url?q=https://github.com/mangudai/sublime-text&sa=D&source=editors&ust=1744981493581360&usg=AOvVaw2sMvsfRm_JY2TvuNKmc2C6) pre-DE

### IntelliJ

* [By](https://www.google.com/url?q=https://plugins.jetbrains.com/plugin/10628-rms-plugin&sa=D&source=editors&ust=1744981493581631&usg=AOvVaw1jzM2UHZtltU-Gdi-fucf6) [hszemi](https://www.google.com/url?q=https://plugins.jetbrains.com/plugin/10628-rms-plugin&sa=D&source=editors&ust=1744981493581721&usg=AOvVaw2EfdvxTkLkp25Gy0xgB_kE) pre-DE

### Atom

* [By twestura](https://www.google.com/url?q=https://atom.io/packages/language-aoe2-rms&sa=D&source=editors&ust=1744981493581934&usg=AOvVaw3uU8EX6uivw9DRpKh6hxcM) pre-DE

### Vim

* [By Renée Kooi](https://www.google.com/url?q=https://github.com/SiegeEngineers/vim-aoe2-rms&sa=D&source=editors&ust=1744981493582136&usg=AOvVaw3Jy-7JqOXCI84no6QRiPBb) pre-DE

### PSPad

* [By chasqui](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D7921&sa=D&source=editors&ust=1744981493582353&usg=AOvVaw1o1p7rpKZ7dAQM4WrJy4fj) pre-DE.  Has context sensitive help and auto-generation of code.

### Word

* [By chasqui](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D8023&sa=D&source=editors&ust=1744981493582642&usg=AOvVaw2tLG7gOHupB3pDB1aILBsg) pre-DE

## Miscellaneous Utilities

* [Image to rms](https://www.google.com/url?q=https://image-to-rms.aoe2.se/&sa=D&source=editors&ust=1744981493582923&usg=AOvVaw1CLZxBSHcI3994ktfH7D4T) - a fun little utility to turn an image into a map script
* [Mod Directory](https://www.google.com/url?q=https://mods.aoe2map.net/&sa=D&source=editors&ust=1744981493583117&usg=AOvVaw3XeDSz420S8gaKcvvkWgUk) - browse and download DE mods without using the official site

---

#

# Appendix

## DE Update Bulletin

Updates/changes/fixes/bugs (relevant to map scripting) from all DE updates are listed here for easy reference.

[The Three Kingdoms Update (April 2025)](https://www.google.com/url?q=https://www.ageofempires.com/news/a-sneak-peek-at-new-content-coming-to-age-of-empires-ii-definitive-edition/&sa=D&source=editors&ust=1744981493583811&usg=AOvVaw1172_L12VoNfitlAi9PESx)

* [Math operations](#h.bqp5f3wcm40e) to use [#const](#h.poaiyxi48mi6) to store numbers and perform simple calculations.
* New attribute for objects: [require\_path](#h.woysch92a2oh).
* [min\_distance\_to\_players](#h.asuv2zzhmbsd) no longer applies a minimum distance to all lands.
* [create\_elevation](#h.h85o0pyielaj) can now go up to 16.
* [enable\_tile\_shuffling](#h.ewsg05tiznb0) is now actually useful to prevent predictable resource spawns in cases where [find\_closest](#h.kzkb7o2yhtk9) is being used with [set\_circular\_placement](#h.15fez3e52vqr).
* The following commands can currently directly accept floating-point values:

* [terrain\_cost](#h.pw0ckpmic7kh)
* [guard\_state](#h.7jvxo0vqwqu8)
* [effect\_amount](#h.1niw1edwqhy5)
* [effect\_percent](#h.7siepjsm3bdc)

* New [objects](#h.nvxriamulybh). Notably the following:

* Huntable chickens (unpushable) with 65 food: WILD\_CHICKEN\_A, WILD\_CHICKEN\_B, WILD\_CHICKEN\_C
* Herdable chickens with 65 food: CHICKEN\_A, CHICKEN\_B, CHICKEN\_C
* ARGALI as a new standard huntable with 140 food.
* New predators: BLACK\_BEAR, POLAR\_BEAR, ARABIAN\_WOLF
* New wild animals (no food): WILD\_HORSE\_B, WILD\_HORSE\_C, WILD\_HORSE\_D, WILD\_HORSE\_E, WILD\_MONKEY, WILD\_PENGUIN
* New trees: LUSH\_BAMBOO\_TREE, ASIAN\_PINE\_TREE, PEACH\_BLOSSOM\_TREE, WILLOW\_TREE, ASIAN\_MAPLE\_GREEN\_TREE, ASIAN\_MAPLE\_AUTUMN\_TREE
* Felled trees: FELLED\_TREE, FELLED\_TREE\_BAOBAB, FELLED\_TREE\_BAMBOO, FELLED\_TREE\_LUSH\_BAMBOO
* New permanent stumps: BAMBOO\_STUMP, BAOBAB\_STUMP, LUSH\_BAMBOO\_STUMP
* New constants for existing objects: FIRE\_TOWER, CRUSADER\_KNIGHT
* Idle villagers for use with [Empire Wars](#h.xzwndngyca0k): idle male villager 1875, idle female villager 1876
* New temporary map revealers: Small (4 LOS) 1872, Medium (10 LOS) 1873, Large (20 LOS) 1874

* Dedicated placeholder objects:

* On-grid generic 1543
* On-grid land 1544
* On-grid amphibious 1545
* On-grid naval 1546
* On-grid water 1547
* Off-grid generic 1902
* Off-grid land 1905
* Off-grid amphibious 1909
* Off-grid naval 1912
* Off-grid water 1921

* New [terrains](#h.3bdjnf7tryyk): PALM\_GRASS\_FOREST (existing, but now has a const), LUSH\_BAMBOO\_FOREST, YELLOW\_SHALLOW\_WATER, YELLOW\_SHALLOW, YELLOW\_DEEP\_WATER, several pasture terrains
* New [cliff type](#h.uow2rvrpkup5) (limestone cliffs).
* New [color correction](#h.ptggu3c4a8jy) types.
* New [attributes](#h.oumcl095iabt): ATTR\_OBSTRUCTION\_TYPE, ATTR\_BLOCKAGE\_CLASS, ATTR\_SELECTION\_EFFECT, ATTR\_ATTACK2\_GRAPHIC, ATTR\_DAMAGE\_REFLECTION, ATTR\_FRIENDLY\_FIRE\_DAMAGE, ATTR\_REGENERATION\_HP\_PERCENT, ATTR\_BUTTON\_ICON\_ID, ATTR\_SHORT\_TOOLTIP\_ID, ATTR\_EXTENDED\_TOOLTIP\_ID, ATTR\_HOTKEY\_ACTION, ATTR\_CHARGE\_PROJECTILE\_ID, ATTR\_AVAILABLE\_FLAG, ATTR\_DISABLED\_FLAG, ATTR\_ATTACK\_PRIORITY, ATTR\_INVULNERABILITY\_LEVEL, ATTR\_GARRISON\_FIREPOWER
* Two new official random maps, and the code for Nomad, Black Forest and Arena has been rewritten. New [included files](#h.t1xmddo9ftb) used by the more recently updated maps.
* Added "quickstart" (9 villager) versions of the most popular maps.

[Battle for Greece Update (October 2024)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-128442/&sa=D&source=editors&ust=1744981493588582&usg=AOvVaw3IFOn4NfA8VzSfnEEuU4ws)

* Added many new [objects](#h.nvxriamulybh) for the new DLC:

* 3 new [civilizations](#h.8ctucmcvyhyv) (unranked and single player only) with a unique antiquity tech tree that significantly overhauls water gameplay in particular.  2 new architecture styles.
* OYSTERS as a gold source that can be placed on water and amphibious terrains and can be gathered from by villagers and fishing ships.  This is the only new object which has a predefined constant.
* The Mouflon (id 2340) as a new deer-equivalent.
* A large number of new decorative gaia objects.

* Added the ANTIQUITY\_MODE [conditional](#h.vs551a7tyxet), which checks for the antiquity mode lobby setting that enables trading for wood. Many of the official maps have been updated to check for this conditional to decide whether to generate oysters.
* Added the CT\_MARBLE to get marble cliffs using [cliff\_type](#h.ydwb5bkkiqmi).
* Full Tech Mode technology attribute flag 26 added, which restricts the tech to trigger only when the Antiquity Mode lobby flag is active.
* Type technology attribute flags 32 and 33 added, the options are now as follows:

* 0: Normal technologies
* 2: Shows research progress in the age up bar
* 32: Building specific upgrade, will only apply the effects to the building it is researched in, and can be researched at multiple instances of the research location separately
* 33: Repeatable technology, can be researched as long as it is available, even if already researched

* Technology cost deduction type flag 2 added, this will only remove a local resource stored on an individual building (paired with Type flag 32)
* Added object Store Mode type 16, which stores the resource as a local resource in that individual copy of the object (used for individual building upgrades)
* Technology effect types 200 and 201 added, with the following effects:

* 200: Set attribute value for the local building where the tech applying this effect was researched from
* 201: Add/subtract from an attribute for the local building where the tech applying this effect was researched from

* Additional effects added to the unit Aura Task (Task type 155). These are parameters for the “Search Wait Time” field, with the following effects:

* 116: Increase melee armor of nearby objects
* 117: Increase pierce armor of nearby objects
* 113: Increases conversion resistance of nearby objects

* Linked Techs describe techs that are associated in some way. They are defined in linkedTechs,json. There are three types:

* Mutually Exclusive Techs – when one tech is researched, the other linked techs will be disabled
* Toggleable Techs – allows you to “enable” one tech in a group of technologies
* Cycle Techs – cycle through a list of techs, applies effects of selected tech and disables the others

* Eras were added to eras.json. Eras allow defining overrides for a civilization. You can override age icons, tech descriptions, and which techs are available in full tech mode. You add the specified era as an option within civilizations.json.
* New “speed charge” attack task added, as task 133. For this to work, the unit’s “Special Ability” field must be set to 3. This task uses the following parameters:

* Work Value 1: Minimum distance from the target for the speed up to start
* Work Value 2: Maximum distance from the target for the speed to start
* Work Range: Multiplier on the unit speed while charging
* Work Flag 2: This must be set to 2001 for the task to work

[April 2024 Update](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-111772/&sa=D&source=editors&ust=1744981493594143&usg=AOvVaw1N9d5S7CN8QoHVvlI-g_NL)

* All scouting units can now use the Auto Scout functionality instead of just the starting one.
* Fixed an exploit where one could avoid cracked terrain bonus damage by constructing and deleting a farm before constructing a building on the cracked terrain.
* Empire Wars Only: Huns now start without both the -100 wood penalty and the pre-generated houses.
* Added eleven new maps that have been created for the Red Bull Wololo: El Reinado tournament

[Victors and Vanquished Update (March 2024)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-107882/&sa=D&source=editors&ust=1744981493595041&usg=AOvVaw0-ztDxYUXh94Nb3h4IkQac)

* [Map sizes](#h.qannz915qgy5) reworked.  New conditionals were added to match the in-game names but the legacy conditionals still work as well.

* The names of in-game map size options now display their base dimension.
* Changed the name of the map size with 240 tiles dimension from Giant to Huge.
* Added MORE\_MAP\_SIZES launch parameter to unlock new map sizes in Editor and Lobbies: Miniature [80], Giant [252], Massive [276], Enormous [300], Colossal [320], Incredible [360], Monstrous [400]. Note that most standard random maps may not correctly support the new map sizes yet.

* The game can now boot directly into the Scenario Editor if the EDITOR launch parameter is specified. This can be combined with other parameters (e.g. EDITOR LAUNCH\_GAME\_VARIANT=AOE1).
* The game will no longer crash when clicking on certain gaia objects (neutral market, granary etc.) while having the extended unit stats option enabled. (unlisted update)
* Resources tracking player stats (such as P1 Kills, Razed by P3, etc.) now support Gaia, and have been relocated to the 300-499 range.
* The x256tech script has been updated to its final version, and a variant called x9tech is now available.

[The Mountain Royals Update (October 2023)](https://www.google.com/url?q=https://www.ageofempires.com/news/preview-age-of-empires-ii-definitive-edition-update-95810/&sa=D&source=editors&ust=1744981493597184&usg=AOvVaw1YRp7Oc3KxLiHgKwT063tj)

* [cliff\_type](#h.ydwb5bkkiqmi) - Added the new cliff\_type parameter for cliff generation, which allows selecting the type of the cliffs to be used on the map. Available options: CT\_GRANITE (default setting), CT\_DESERT, CT\_SNOW.
* Units and other objects (such as resources) are now able to be placed under the TC without the need for placeholder objects.
* Added second variations (different rotations) to all 3 Pavilions.
* Added smaller Bridge A/B pieces, allowing more control over the bridge shape.
* New DLC objects

* Note that giving a fortified church to players via the map script will not let them research or train anything there.
* Armenians get a free relic with their first fortified church.  On maps with 0 relics (ex. forest nothing), relic spawn can be turned off by disabling tech 957 in the map script.  Otherwise Armenians can get an easy relic win.

* Value of Resource 270 now determines the repair cost of siege weapons and ships.
* Value of Resource 271 now determines the repair cost of buildings.
* Value of Resource 272 now allows modifying the damage received by own units when attacked from higher elevation.
* Value of Resource 273 now allows modifying the damage received by own units when attacked from lower elevation.
* Allowed military units to have conversion ability if they have conversion tasks and the value of resource 279 for the player is higher than 0. The conversion button will appear on the 15th button ID in the command panel; the hotkey can be modified in Military Units hotkey group. The conversion range of military units is controlled by Work Range value in their conversion tasks plus the value of resource 280. Value of Resource 281 determines the conversion success chance per conversion round. Value of Resource 282 determines the faith recharge rate after a successful conversion.
* Units can now be spawned garrisoned if at the moment of spawning the value of resource 283 for the player is higher than 0.
* Allowed military units to heal other units similar to Monks if they have heal tasks.
* Added new Combat Ability attribute flag 64 which allows the unit with power up tasks to power up itself (receiving power up from the units set in the power up tasks). If the unit has several power up tasks, all except the first task need to have Auto Search attribute set to 1.
* Allowed making objects with solid obstruction (for example buildings) passable by setting their Unit Size Z attribute to 0.

[June Update (2023)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-87863/&sa=D&source=editors&ust=1744981493600333&usg=AOvVaw2U5niI4cMByCMVTLJEnQCZ)

* Added a new flag 4 for Blast Attack Level attribute which can disable friendly damage for ranged units with blast attack.
* Undocumented updates at some point prior to June 2023:

* [zone](#h.li85mvsiskop) 99 no longer crashes the game
* [color\_correction](#h.7xt01aajnkw9) works again
* [create\_actor\_area](#h.u28jmnfojke3) now no longer has the limitations where it only worked with player objects belonging to player 1
* actor areas with a radius of 0 can now be correctly placed in if [set\_tight\_grouping](#h.ksq6iglmnili) is used.

[Return of Rome Update (May 2023)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-83607/&sa=D&source=editors&ust=1744981493601326&usg=AOvVaw3yZq70AQ-6vgJm0B_MyMKd)

* Romans civilization available with purchase of Return of Rome DLC.
* DE\_GAME\_ROME and DE\_GAME\_AGE2 to check for AoE1 vs AoE2.
* SOLID\_FARMS to check for the lobby option of the same name in AoE1.
* New regional unit: Dromon (anti-building siege warship).
* Previously existing Centurion and Legionary units have been renamed into Imperial Centurion and Imperial Legionary.
* The area healing effect (used by Caravanserai and Stronghold unique technology) no longer stacks from several effect-providing buildings next to each other.
* [nomad\_resources](#h.fj85jt1i1f2l) parameter now reimburses the Town Center’s cost (with the cost bonuses taken into account) instead of always adding 275 wood and 100 stone to the starting resources.
* GAZELLE (id 1796)  – a new prey animal unit (like a deer)
* The behavior of predator animal class units is now controlled by Combat Level attribute: 1: boar-like, 4: wolf-like.
* Added new attributes to control previously hardcoded properties:

* ATTR\_MIN\_CONV\_MOD (adds to the minimum time to convert the unit).
* ATTR\_MAX\_CONV\_MOD (adds to the maximum time to convert the unit).
* ATTR\_CONV\_CHANCE\_MOD (reduces the chance to convert the unit per conversion roll).
* ATTR\_FORMATION\_CATEGORY (0: not using formation, 1: mobile, 2: body, 3: ranged, 4: long ranged, 5: protected).
* Formation Spacing (controls the spacing between units when in formation).
* ATTR\_AREA\_DAMAGE (multiplier to the percentage of blast damage the non-directly targeted units receive if positive value, fixed number damage if negative).

* Removed Blast Attack Level attribute flags 4, 8, 16, 32 as their functionality is now handled by the new Blast Damage attribute.

* Allowed modifying several more unit attributes by Effect Amount, Modify Attribute trigger effect and technologies in data. Check tooltips in Advanced Genie Editor for more information about them.

* ATTR\_CAN\_BE\_BUILT\_ON (see AGE).
* ATTR\_FOUNDATION\_TERRAIN (see AGE).
* Graphic IDs ATTR\_ATTACK\_GRAPHIC, ATTR\_STANDING\_GRAPHIC, ATTR\_STANDING2\_GRAPHIC, ATTR\_DYING\_GRAPHIC, ATTR\_UNDEAD\_GRAPHIC, ATTR\_WALKING\_GRAPHIC, ATTR\_RUNNING\_GRAPHIC, ATTR\_SPECIAL\_GRAPHIC.

* ENABLE\_TECH and GAIA\_ENABLE\_TECH used by Effect Amount (ID 7, -8 for gaia) has been replaced by SPAWN\_UNIT and GAIA\_SPAWN\_UNIT, which functions similarly to the data version of this effect type. MODIFY\_TECH can now be used instead of ENABLE\_TECH.
* MODIFY\_TECH effect is now able to ATTR\_SET\_STATE of technology. It can be used to disable, enable, force enable or research the specified technology ID.
* ATTR\_RESEARCH added.
* Relic-requiring technologies are no longer hardcoded to IDs 699-703 (used by the Lithuanian cavalry attack bonus). To receive this functionality a technology needs to have its first cost type set to Relics Captured.
* The unit cost addition (multiplying the cost attributes by -1) or removal (multiplying the cost attributes by -2) can now be used by technology effects in data.
* Data mods are now better supported, including these changes which relate to rms:

* It is now possible to define custom random map pools through maps.json in data mods.
* Mod-specific loading symbols can now be defined for random maps in the string 8739.
* It is now possible to include widgetui/morematerials.json in a non-data mod which will add material definitions on top of the original materials.json file.

* The ice beach terrain (ID 37) now uses a unique texture.  Ice shallows and solid ice still share a texture.

[April Update (2023)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-81058/&sa=D&source=editors&ust=1744981493671790&usg=AOvVaw2BpJzcAlS4sqtW9EbvOiw-)

* [override\_map\_size](#h.sdzu3ermj1ah) - adjust the map size to anything in the range 36-480.

* This is used by the following official maps to make them one size larger: Archipelago, Islands, Migration, Team Islands, Fortress, Budapest, Pacific Islands, and Sandbank

* [generate\_for\_first\_land\_only](#h.c3yp8xxihcnd) - used on the official double and triple TC maps to only generate one king.
* [set\_facet](#h.qbzrlsoh7lg7) - to manually pick a frame/rotation/appearance for an object.
* It is now possible to update all your created mods in-game if you have more than 50 mods.

[August Update (2022)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-66692/&sa=D&source=editors&ust=1744981493672912&usg=AOvVaw17nmwivLCo4UhqIigz4WfN)

* Added the new [set\_building\_capturable](#h.svu8loj25dpl) RMS parameter, in order to enable Battle Royale building behavior (allowing the building to be captured many times) in other game modes (without having to upgrade from a monument).
* New Red Bull Wololo tournament maps added (Shoals and Morass).
* Removed reaction distance modifier for predator animals depending on difficulty and made it so that predator animals always find villagers within 6 tiles and other units within 4 tiles. Easiest difficulty on scenarios and campaigns will still use 4 tiles.
* Importing Local Mods doesn’t break Subscribed Mods anymore.
* XS files now transfer correctly on either Subscribed or Local Mods (but still don't work for spectators).

[April Update (2022)](https://www.google.com/url?q=https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/&sa=D&source=editors&ust=1744981493674003&usg=AOvVaw3RHap2E9u6a_D6CGr0rkmc)

* [beach\_terrain](#h.qlmjwkuqe8hc) - place custom beaches in [create\_terrain](#h.acnibljecbfg) commands when the created terrain borders water.
* [set\_circular\_placement](#h.15fez3e52vqr) - changes [min\_distance\_to\_players](#h.asuv2zzhmbsd) and [max\_distance\_to\_players](#h.v2aq68odkdzl) to use the circular (Euclidean) distance, rather than a square radius.
* [min\_distance\_to\_map\_edge](#h.w2q69orjs3l3) - keeps objects away from the edge of the map.
* [find\_closest\_to\_map\_center](#h.c8jwpxwfx68p) - place the object on the closest free tile to the center of the map.
* [find\_closest\_to\_map\_edge](#h.mmr1mgkocjlx) - place the object on the closest free tile to the edge of the map.
* ATTR\_SET\_STACKING\_RESEARCH\_CAP - Set a limit on the number of times techs can be stacked when ATTR\_SET\_STACKING is active.
* ATTR\_FOG\_FLAG - set the fog visibility of an object.  0 Not visible, 1 Always visible, 2 Visible if alive, 3 Inverted visibility, 4 Check doppelganger
* Added 1 new [terrain](#h.3bdjnf7tryyk) - palm forest on grass
* Added new DLC [objects](#h.nvxriamulybh)
* ATTR\_GARRISON\_TYPE has new flags: 16: livestock, 32: siege units, 64: ships
* Added ATTR\_SET\_HOTKEY, ATTR\_STORAGE2\_VALUE, ATTR\_STORAGE3\_VALUE, ATTR\_OCCLUSION\_MODE, ATTR\_RADIUS\_3, ATTR\_MAX\_CHARGE, ATTR\_RECHARGE\_RATE, ATTR\_CHARGE\_EVENT, ATTR\_COMBAT\_ABILITY, ATTR\_ATTACK\_DISPERSION, ATTR\_PROJECTILE2\_ID, ATTR\_BLOOD\_ID, ATTR\_HIT\_MODE, ATTR\_VANISH\_MODE, ATTR\_PROJECTILE\_ARC, ATTR\_POPULATION
* ATTR\_CHARGE\_TYPE new options: 3: charge area attack, 4: agility
* ATTR\_COMBAT\_ABILITY new attribute to control several combat unit properties: 1: ignore melee and pierce armors of the targeted unit, 2: resist armor-ignoring attacks, 4: damage the targeted unit’s armor (Obuch ability), 8: attack ground ability, 16: bulk volley release (siege units, kipchaks)
* ATTR\_TRAITS has new flags: 8: transformable unit, 16: scout unit
* ATTR\_PIECE controls the constructable building ID for units with trait flag 4, transform unit ID for units with trait flag 8
* Added new flag 128 for ATTR\_BLAST\_LEVEL attribute which limits the blast attack area of the unit to the direction it is facing when attacking
* [enable\_tile\_shuffling](#h.ewsg05tiznb0) added for [create\_object](#h.2vz7nxt2afqo)
* It is no longer necessary to first record a game in order to open it with [CaptureAge](#h.24lmsw81mk8g)
* [force\_nomad\_treaty](#h.13why2qs1rix) no longer causes recorded games to go out of sync
* Khmer no dropsite farmers bonus is now controlled by resource 96
* The amount of Town Centers which are allowed to be constructed before they are enabled by technology is now controlled by Early Town Center Limit resource (ID 218)
* Starting scout unit ID is now controlled by resource 263
* Added new resources which can enable secondary incomes (wood, food, stone) from trade and relics

[January Update (2022)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe-ii-de-update-58259/&sa=D&source=editors&ust=1744981493677960&usg=AOvVaw1g6zDBuFQIROAz5GO0mrTJ)

* [ignore\_terrain\_restrictions](#h.fx1jh8glz0tl) - allow objects to be placed on terrains they normally cannot be placed on.
* [make\_indestructible](#h.a9ken9hkekd6) - make a building unable to be attacked
* ATTR\_ATTACK and ATTR\_ARMOR now require multiplying the attack/armor class by 65536 instead of 256

[November Update (2021)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoeii_de_update_56005/&sa=D&source=editors&ust=1744981493678605&usg=AOvVaw0ypZkYFCiJhsD_h6KvkNeO)

* [force\_nomad\_treaty](#h.13why2qs1rix) - adds a treaty that lasts 5 min or until every player has completed a town center.
* [override\_actor\_radius\_if\_required](#h.4t8s9kqehrvb) - used to allow folwarks to spawn adjacent to berries in Empire Wars even though they are larger than mills
* Added a search box to the map selection screen.
* The map selection screen now allows you to press a letter to jump between maps that start with that letter.
* Arabia is now based on the King of the Desert tournament version (and is now a very complicated script to look at)
* Mod thumbnail images can now be in both PNG and JPG formats.
* Secondary game modes ([King of the Hill](#h.wcxqrcy4fp9f), [Regicide](#h.z4ap3pncwpvh), [Empire Wars](#h.xzwndngyca0k)) can now be selected from the victory tab in the scenario editor.  (useful for testing)
* Show simple tooltips for units enabled by [effect\_amount](#h.1niw1edwqhy5), which don’t usually show tooltips (e.g. when enabling sheep to be trained in a mill, a tooltip can now show the cost of the unit).
* Fixed a rare crash in the Scenario Editor when repeatedly generating maps with specific characteristics.

[October Update (2021)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoeii-de-update-54480/&sa=D&source=editors&ust=1744981493680349&usg=AOvVaw2UuDToFNjCnTpQMqxQfJ0Y)

* Feitoria and Trade Workshop productivity now use separate sets of resources (205-208 and 242-245, respectively)
* The [constants](#h.cym0hd55425r) for the Trade Workshop resource trickle are now pre-defined
* More maps from the Red Bull Wololo tournament are now officially part of the game
* The [min\_connected\_tiles](#h.6rc3lgpd171k) parameter now properly works for all players when using [behavior\_version](#h.seeuqpcozayb) 2.  But it is still buggy overall.

[Dawn of the Dukes Update (August 2021)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoeiide-update-51737/&sa=D&source=editors&ust=1744981493681175&usg=AOvVaw2mcNO7gITHEcrvy_b5cla8)

* Added [create\_actor\_area](#h.u28jmnfojke3) to create actor areas without creating a (placeholder) object
* Added 2 new [terrains](#h.3bdjnf7tryyk)
* Mud [terrain](#h.3bdjnf7tryyk) is now brown on the minimap (was green)
* "Fixed a performance issue that occurred during the first few seconds of gameplay on many Random Map Scripts"
* A new [color\_correction](#h.7xt01aajnkw9) (night) is available
* New [objects](#h.nvxriamulybh) (units, heroes, buildings) from the DLC are added
* Arabia terrain and objects generation overhauled

[July Update (2021)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-50292/&sa=D&source=editors&ust=1744981493682129&usg=AOvVaw2bSvDZr4_rOGcI7xvyxakc)

* [min\_connected\_tiles](#h.6rc3lgpd171k) and [accumulate\_connections](#h.bd2l5930vfzf) added
* Implemented [guard\_state](#h.7jvxo0vqwqu8) from UP
* ATTR\_SET\_NAME ATTR\_SET\_DESCRIPTION ATTR\_SET\_STACKING added
* Red Bull Wololo maps added and their Empire Wars standards adopted
* [Custom map icons](#h.ttumfg1xstsg) are now possible by just including a png of the same name in the same folder as your map!
* Direct placement maps no longer break random placement maps in the scenario editor!
* [set\_avoid\_player\_start\_areas](#h.ijxhxwahit2u) now allows using a distance parameter
* Fixed a bug where maximum value in [rnd(min,max)](#h.ml72cdygzrfv) was exclusive if min was 0
* [actor\_area\_to\_place\_in](#h.d6d6k8uc57zx) no longer disables [max\_distance\_to\_players](#h.v2aq68odkdzl)
* [force\_placement](#h.138scj5wa7v7) in small actor areas no longer produces excess objects
* [place\_on\_forest\_zone](#h.38vodsu87lbp) now correctly places buildings larger than 1×1 tiles
* Packing a Town Center in [Battle Royale](#h.yaqdimuqjsaj) now works correctly and no longer causes a crash.  Also, packed town centers can no longer be unpacked on obstructions
* Fishing Ships now automatically start working in [Empire Wars](#h.xzwndngyca0k)
* Laming straggler trees is no longer possible unless a villager actually begins construction
* Dolphin can no longer be built on
* Tatar sheep, Chinese and Mayan villager, and Inca llama spawn bonuses now work correctly on nomad starts in Castle age or higher
* Sea Walls now generate Sea Gates
* Scripts using many actor areas will load (slightly) faster
* Fixed an issue that caused scripts using a small [actor\_area](#h.obv5ypy66a57) to occasionally fail to spawn the desired number of objects.
* The hero status attribute now controls hero glow. Hero glow now appears for units with full hero status (1) or with the new hero glow flag (64).
* Added a new Hero Status flag (128) which can invert properties of other Hero Status flags assigned to the unit (except flag 1).
* The Regeneration Rate attribute now affects units with hero regeneration. The rates from both regenerations sum with each other.
* The tech modification trigger effects added in our November Update, including Change Technology Name, Change Technology Description, and Enable/Disable Technology Stacking can now be used with the MODIFY\_TECH effect in effect\_amount.

[April Update (May 2021)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-47820/&sa=D&source=editors&ust=1744981493685466&usg=AOvVaw1fW0tXHbTclahEx-LD3x_0)

* ATTR\_BLAST\_DEFENSE ATTR\_HOTKEY\_ID ATTR\_REGENERATION\_RATE added
* Added new flags for Hero Status attribute to control hero properties individually:

* 2: cannot be converted
* 4: auto-healing
* 8: default defensive stance
* 16: protected formation
* 32: safe delete confirmation
* The flags can be combined with each other, or flag 1 can be used to enable full hero status.

* The Regeneration Rate attribute now determines the number of hit points a given unit regenerates in a minute. The Regeneration task in the unit data is no longer required. The Regeneration Rate attribute has no effect for units with Hero Status flag 1 (full hero status) or 2 (auto-healing), which regenerate at the fixed 30 hit points/min rate.

* Scenario editor should now longer crash when reducing the map size.

[March Update (2021)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-46295/&sa=D&source=editors&ust=1744981493687126&usg=AOvVaw2ZBCjeBih1vOE08YASOofM)

* Scenario editor black terrain crashes fixed (other occasional crashes still occur)
* [effect\_percent](#h.7siepjsm3bdc) fixed

[Lords of the West Update (January 2020)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoeiide-update-44725/&sa=D&source=editors&ust=1744981493687595&usg=AOvVaw1kKdMF-iatFSgQGP73Y56x)

* Scenario Editor STILL broken - use the singleplayer to test instead
* [effect\_amount](#h.1niw1edwqhy5) fully implemented - please report any bugs you discover.
* [effect\_percent](#h.7siepjsm3bdc) implemented - But is bugged in that it rounds too early
* In [King of the Hill](#h.wcxqrcy4fp9f) games, resource generation via Monuments is now enabled by default.

* It can supposedly be turned off by using [effect\_amount](#h.1niw1edwqhy5) to disable technology 729, but I have not been able to confirm this.
* You can now remove the monument resources object (1639) from all of your maps, because it is no longer necessary.

* [#includeXS](#h.w4knc4t4en6w) has been added to load .xs scripts for random maps. Official documentation: [.xs scripting in Age of Empires II: Definitive Edition](https://www.google.com/url?q=https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/xs-scripting-in-age-of-empires-ii-definitive-edition&sa=D&source=editors&ust=1744981493688929&usg=AOvVaw33MGrvmfh0Cpj5pBps8qzv); community documentation: [XS Scripting For Beginners](https://www.google.com/url?q=https://divy1211.github.io/AoE2DE_UGC_Guide/general/xs/beginner/&sa=D&source=editors&ust=1744981493689144&usg=AOvVaw12Ucnsp9p_EBfSmL7TE9Xx)
* Many new constants were defined, including all the relevant effect constants, and constants for feudal/castle/imperial -age versions of buildings (see: [Constant Reference](#h.9iqqcke3biv))
* Two new civilizations added, along with the associated units and objects (see: [Objects](#h.nvxriamulybh))
* Great Fish (Marlin) can no longer be deleted by Dock foundations

[Anniversary Update (Nov 2020)](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-42848/&sa=D&source=editors&ust=1744981493689803&usg=AOvVaw1ovl1aNY6FRUDh9MHA4AeC)

* Empire Wars standard villager distribution changed (less on farms), and sheep removed
* [behavior\_version](#h.seeuqpcozayb) command added
* [Conditionals](#h.vs551a7tyxet) for starting age added
* Scenario Editor broken - use the singleplayer to test instead
* [Battle Royale](#h.yaqdimuqjsaj) game mode implemented, along with one new terrain.

[August 2020 Update](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-40220/%23&sa=D&source=editors&ust=1744981493690438&usg=AOvVaw2ksM7-dI5vb3IvvpjRi1i9)

* The map seeds from recorded games can now be used to generate the same map in the Scenario Editor.

[May 2020 Update](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-37650/%23&sa=D&source=editors&ust=1744981493690726&usg=AOvVaw1pzsbRcUgPNqsz0wMq59kL)

* The [number\_of\_tiles](#h.bzvr6x5i10na) and [land\_percent](#h.ipg3ruf70nn4) commands no longer create larger lands than intended. (This affected a few standard maps, such as Arena.)

[April 2020 Update](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-36906/&sa=D&source=editors&ust=1744981493691115&usg=AOvVaw30UddPm-puMOZHoaAWdJxH)

* Maps using [resource\_delta](#h.ndaw6icg9cnp) will now accurately display HP bars over resources.
* Increased the limit of objects and lands that can be generated through RMS from 99 to 100,000.
* Added [enable\_balanced\_elevation](#h.izx21xcrwjlg) command to improve hill generation in Random Map Scripts.
* Added [effect\_amount](#h.1niw1edwqhy5) to modify resource values (such a starting resource) through RMS.

[February 2020 Update](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-35584/%23&sa=D&source=editors&ust=1744981493691925&usg=AOvVaw1pP5XYYB_LLDwUghu9RcgJ)

* Capture the Relic: The game will no longer spawn a second Monastery if the map has already spawned one for a player.
* Capture the Relic: Fixed an issue where Monasteries could spawn into the map with a “more on-fire than intended” amount of health.
* [Regicide](#h.z4ap3pncwpvh): Will now properly adjust resource numbers based on whether the host chooses Low, Standard, or High resources. (Infinite is still infinite.)
* [assign\_to](#h.b6uul7n11c6g) command has been added. This can be used to assign a land to a player, color, or team in combination with [direct\_placement](#h.jbnjt99zhiqx).
* The Random Map game mode can now be detected using the RANDOM\_MAP identifier.
* One big change for the modding community is the ability for users to publish their mods as Unlisted: An Unlisted mod is not publicly available for users to find and download. It will, however, download automatically when a user joins a lobby where the mod is being run.

[January 2020 Update](https://www.google.com/url?q=https://www.ageofempires.com/news/aoe2de-update-34699/%23&sa=D&source=editors&ust=1744981493693144&usg=AOvVaw3-S7h4YF3qSLTuGrZ2qZn4)

* [King of the Hill](#h.wcxqrcy4fp9f): The monument now generates resources for the controlling player.
* Sudden Death can now be used as an identifier for custom RMS scripts.
* Random maps can now place buildings on terrains without terrain restrictions.
* Random maps now generate the correct Gate types for all Wall types.
* Capture the Relic: Custom Nomad scripts will now allow the player to build a Monastery if the map doesn’t start with one.
* Testing Random Map Scripts in the scenario editor now works correctly when teams are set using diplomacy settings.
* A new command [avoid\_cliff\_zone](#h.t2916w9l2cff) has been added to help prevent objects from appearing too close to cliffs. The distance can be set by using the same format as the [avoid\_forest\_zone](#h.ym7v1j9vbnle) command.
* Fixed an issue where setting [land\_percent](#h.ipg3ruf70nn4) to 100 would occasionally fail to generate land on all available tiles. (For example, this would sometimes result in random patches of water on Highland.)
* The command, [set\_scaling\_to\_player\_number](#h.l48a16uing0q), now works correctly when a map is generated in the scenario editor.
* The command, [circle\_radius](#h.lc3eipzhfx0z), now supports a secondary value to define the variance of the circle. For example, circle\_radius 20 1 would create a circle with radius 20 and variance 1.
* The file random\_map.def now includes several new terrain constants:

* ICYSHORE
* DLC\_WETROCKBEACH
* DLC\_GRAVELBEACH
* DLC\_WETBEACH
* DLC\_REEDSBEACH
* MEDITERRANEAN\_FOREST
* CYPRESS\_TREE
* ITALIAN\_PINETREE
* OLIVE\_TREE

## AoC Color Palette

![](images/image6.png)

## Magic Numbers

A few noteworthy numbers.

9320 - the maximum number of objects/clumps that can be scaled to map size without breaking for ludicrous map size.

32768 = 2^15 - the maximum unit HP. Also the maximum amount of resources per node (pre-DE)

Also the maximum value that can be used in [effect\_amount](#h.1niw1edwqhy5) (pre-DE).

16777216 = 2^24 - the maximum value that can be accurately stored with [#const](#h.poaiyxi48mi6) in DE.

2147483647 = 2^31 - the maximum amount of resources per node in DE (with [resource\_delta](#h.ndaw6icg9cnp)).

4294967296 = 2^32 - the maximum [terrain\_cost](#h.pw0ckpmic7kh) that seems to change connection behavior.

-949671966 - a number that gives a highly regular pattern for [clumping\_factor](#h.7e3knrokkcni) (lands) due to unknown (algorithmic) reasons.

## DE Constant Translations

The lead random map scripter at Forgotten Empires is Czech, consequently some of the constants used might not make sense to an English speaker.  Below are the main shared constants used by the standard maps (and defined in F\_seasons.inc so that they can vary for each season.)

* HERDABLE\_A: close sheep or other convertible animals
* HERDABLE\_B: further sheep or other convertible animals
* LURABLE\_A: Boar or similar animal that can be lured
* LURABLE\_B: Boar or similar animal that can be lured
* HUNTABLE: Deer or other passive huntable animals
* PREDATOR\_A: wolf or aggressive animal
* PREDATOR\_B: wolf or aggressive animal
* BIRDS\_A: a hawk or other type of bird
* BIRDS\_B: a hawk or other type of bird
* MELKARYBA: small fish, ie. shore fish or box turtles
* FISH\_A: a type of standard fish (225 food)
* FISH\_B: a type of standard fish (225 food)
* KERICEK: berry or fruit bushes
* VODA: water
* MELCINA: shallows
* CESTA: path/road
* WOODIES: primary forest
* WOODIES\_B: secondary forest
* WOODIES\_C: tertiary forest
* LAYER\_A: main terrain
* LAYER\_B: secondary terrain (used for patches)
* LAYER\_C: tertiary terrain (used for patches)
* LAYER\_E: further land terrains
* LAYER\_F: further land terrains
* STRAGGLER: individual tree
* BLANKOBJECT: invisible placeholder used to help spread out resource generation

## Evil Fog Terrain Texture Specifications

This information concerns the evil fog terrain (ID 69) texture, added in DE for Battle Royale. The information below is from the developer StepS.  It is not relevant for random map scripting, but could be useful if you wish to make a terrain texture mod.

* there are several thresholds for alpha
* maximum opaqueness is 0.75 (192/256) that is the dark background
* maximum alpha for the cracks is <0.5 (127/256) that are filled with blood
* meaning, 128-192 are interpreted as something that does not need to be filled with blood, yet still needs red fog treatment
* 0-127 meaning it is filled with blood
* I have a tool that converts a grayscale DDS into this with configurable white threshold
* where white is background, black foreground
* (in the process everything becomes opacity levels of black)
* basically you have two levels, the background in the 128-192 alpha range and  the foreground in 0-127

[white\_to\_corruption\_alpha.exe](https://www.google.com/url?q=https://www.dropbox.com/scl/fi/7uehr4po1lrkpv7ou6p0n/white_to_corruption_alpha.exe?rlkey%3Dfkisy4jy0af3zcynldd1kgwlx%26dl%3D1&sa=D&source=editors&ust=1744981493701270&usg=AOvVaw1bZDOxslfAQ0AOdjNiAIzs)

[testtexture.dds](https://www.google.com/url?q=https://www.dropbox.com/scl/fi/t3m8trw7im8evq085tb72/testtexture.dds?rlkey%3D9lvvs46zdfsvlfbv3crkjjytg%26dl%3D1&sa=D&source=editors&ust=1744981493701493&usg=AOvVaw35Edidw2eXxbyUMvWaoMNQ)

* it supports only the dds in that format and no mipmaps
* you can specify white threshold, that means values of white after a certain maximum will be flattened to the max of the "background" range
* basically white level of 255 (default threshold) means it will become 192, aka the background
* while anything below 255 will be divided by 2, to become part of the 0-127 alpha, aka the blood
* if the threshold is set at lower values that means higher whites are all flattened to 192
* If someone wants to reimplement this conversion it's really simple. Basically do something like this on every pixel in the DDS

a = r < threshold ? r / 2 : 192;

r = 0;

g = 0;

b = 0;

* you can experiment with spreading the bg across the 128-192 range too

## Temporary Map Location

In AoC and HD, maps are transferred from the host to the client and end up in the main random maps folder within your game directory.  The advantage of this is that you can easily find any custom map you ever played on.  The disadvantage is that you will get a desync if your map has the same name but is different from the host's version.

In DE, maps are instead transferred to AppData\Local\Temp\resources\\_common\random-map-scripts where they are only stored until you exit the game.

## String Dump from the exe

This information may or may not give some insight into how the random map generator code actually works internally:

[String dump from the exe](https://www.google.com/url?q=https://docs.google.com/document/d/1TktXHUg33JfjRyiR-skhs8vSRj-4fGGkneJErckyzD8/&sa=D&source=editors&ust=1744981493703558&usg=AOvVaw2JorSq9xNFQw_SWdE7IpQX)

## Non-Functional Syntax

These things were discovered by searching the non-localized-key-value-strings-utf8.txt file in HD/DE.  None of these appear to do anything, based on what is currently known.  If you discover anything, please let me know!

#undefine

#include

min\_distance

max\_distance

set\_position

percent\_of\_land

## Balanced Elevation Comparison

![](images/image3.png)

Courtesy of T-West

## Circle Radius Comparison

![](images/image2.png)

Courtesy of T-West

## Special Note for WololoKingdoms HD

Some of the existing terrains are changed.  The predefined constants have been updated, but if you are defining manually (with [#const](#h.poaiyxi48mi6)), you will need to address it manually yourself.  See also [WololoKingdoms Terrain Conversions](https://www.google.com/url?q=https://github.com/SiegeEngineers/WololoKingdoms%23terrains&sa=D&source=editors&ust=1744981493704907&usg=AOvVaw2C454MbhQhKI3udU5KfaI-)

* Terrain 11 (formerly dirt2) is now mangrove shallows, but you can use terrain 27 (foundation dirt) to get the same look.
* Terrain 38 (formerly snow road) is now cracked dirt, but terrain 33 is now snow road, so you can use that.
* Terrain 33 (formerly snow dirt) is now snow road but you can use terrain 36 (foundation snow) to get the same look.
* Terrain 20 (formerly oak forest) is now mangrove forest, but you can use terrain 10 (forest) to get the same look.
* Terrain 16 (formerly cliff grass) is now baobab forest, but you can use terrain 0 (grass) for the same look, or pick a new terrain of your choice.
* Terrain 41 (formerly buggy and unused) is now acacia forest.

## Zipped Random Maps (UP Only)

UserPatch 1.5 allows players to create ZR maps.  These are zip files containing an rms, as well as potentially a scenario (scx) and/or custom terrain textures (in the slp format).  This allows you to create "Real World"-style maps for UserPatch.  The scenario takes the place of the land generation section and can be used to place terrains and objects as well.  The rms then acts on the scenario.  This is only supported on the UserPatch.

### UP ZipRmsFiles Documentation

(from \Reference\Scripting\ZipRmsFiles.txt within your [UserPatch](https://www.google.com/url?q=http://userpatch.aiscripters.net/guide.html%23&sa=D&source=editors&ust=1744981493706538&usg=AOvVaw0UYj-d99vckUixwgUlB3jk) install directory)

;--------------------------------------

; Zip Random Map Script Notes

;--------------------------------------

To create a valid zip-rms (ZR) file, please note the following:

- you must include 1 valid rms text file

- you can include 1 scx file if this will be a Real World Map

- you can include any terrain override slps between 15000.slp and 15049.slp

- add all of these files into a zip file with no compression (store)

- there should be no folder paths for files within the zip file structure

- name the zip file "ZR@YourMapName.rms" (change extension from .zip to .rms)

- the ZR@ prefix is required for the game to load a zip-rms file

- place the new rms file into your Random folder (or Script.RM for expansions)

- select it from the Custom map list and play the game as usual

To generate the rms zip with the 7zip command line tool, 7z.exe:

- 7z.exe a -mx0 -tzip "ZR@YourMapNameHere.rms" your-map.rms your-map.scx 15000.slp 15002.slp

;--------------------------------------

; Custom Real World Map Notes

;--------------------------------------

To create a real world map zip-rms, please note the following:

- the rms file should not have <LAND\_GENERATION> unless direct\_placement is used

- the direct\_placement system is provided by default for all custom real world maps

- if direct\_placement is used, please see below for <LAND\_GENERATION> details

- the scx file should have 1 town-center per player to set starting positions

- you can only generate the rms part of ZR@ maps in the scenario editor

- for King of the Hill, you can place a gaia monument on the scx map

- trees and other gaia objects like gold can be placed on the scx map

- other than town-centers, no player objects should be placed on the scx map

- players are placed randomly if the Team Together option is unchecked

- players are placed sequentially (first is random) with Team Together checked

- you must use Team Together if less than 8 starting positions are defined

To have proper team placement for 1v1, 2v2, 3v3, or 4v4 games:

- enable Team Together to place players sequentially (first location is random)

- alternate team numbers on the setup screen: 1, 2, 1, 2, 1, 2, 1, 2

- to support all team setups, place players in the scx like this:

\_\_3\_\_

\_5\_7\_

1\_\_\_2

\_8\_6\_

\_\_4\_\_

;--------------------------------------

; Direct Placement Notes

;--------------------------------------

To use direct\_placement in the rms of a real world map:

- include a <LAND\_GENERATION> section in your rms file

- do not include a town-center for each player in your scx file

- under <LAND\_GENERATION>, add this: base\_terrain REAL\_TERRAIN

- use assign\_to\_player and land\_position to place each player with create\_land

- use X\_PLAYER\_GAME consts like 8\_PLAYER\_GAME with "if" to adjust the layout

#const REAL\_TERRAIN -1

<PLAYER\_SETUP>

    direct\_placement

    ai\_info\_map\_type BLACK\_FOREST 0 0 0

<LAND\_GENERATION>

    base\_terrain REAL\_TERRAIN

if 2\_PLAYER\_GAME

    create\_land

    {

            land\_percent 2

            base\_size 6

            assign\_to\_player 1

            land\_position 25 25 /\* toward the left of the map \*/

    }

    create\_land

    {

            land\_percent 2

            base\_size 6

            assign\_to\_player 2

            land\_position 75 75 /\* toward the right of the map \*/

    }

endif

### Screenshot of how to create a Zipped RMS

![](images/image7.png)

[Link to the full-sized image](https://www.google.com/url?q=https://cdn.discordapp.com/attachments/488354271260180501/498989591425187860/ZippingZRmaps.png&sa=D&source=editors&ust=1744981493712430&usg=AOvVaw2HpLQlQ9jwdEOu0KtWFFC9)

## Miscellaneous Links

Additional outdated links can be found archived in this [post](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D28,42485,,365&sa=D&source=editors&ust=1744981493712834&usg=AOvVaw3cC4Du3i3k2vg3TOd_Afah)

### Older Lists and Spreadsheets

Will be missing info on DE

* [Terrain Reference Sheet](https://www.google.com/url?q=https://www.dropbox.com/s/9rsyu7ph2u6m0oc/Terrain%2520Reference%2520Guide.zip?dl%3D0&sa=D&source=editors&ust=1744981493713161&usg=AOvVaw2EJ2W2X2ADxnq19CyjZT5I)
* [Terrain Names Spreadsheet](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D12226&sa=D&source=editors&ust=1744981493713321&usg=AOvVaw3ZCZV2xUuvEgMvTCL7g58D)
* [Definitive Constants List](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D12000&sa=D&source=editors&ust=1744981493713469&usg=AOvVaw3Sm5RtNtf92rE_ZZ2mpT_b)
* [Advanced Constant Numbers List](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D8724&sa=D&source=editors&ust=1744981493713624&usg=AOvVaw1zXAAdO77a7TBifY-SNIg5)
* [Complete Constant Lists](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D5810&sa=D&source=editors&ust=1744981493713788&usg=AOvVaw0cttsim00vUzxdYiR-_YSi)

### Older Guides

Dated, and may no longer be accurate

* [New RMS Stuff](https://www.google.com/url?q=https://docs.google.com/document/d/1eXRO5ZoSwrVn_rwyVx4k3FhAmqBwRVVzs95OPyIOrd0/edit&sa=D&source=editors&ust=1744981493714077&usg=AOvVaw2kx8emBcHUgfnO5i0hrnUI) a temporary doc that I made to cover all the things that were new in DE

* Checking your map [Long version](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,35724,0,all&sa=D&source=editors&ust=1744981493714342&usg=AOvVaw3mGIr1_7OI7H6z1HWImXVr)[Short version](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D4,35725,0,all&sa=D&source=editors&ust=1744981493714526&usg=AOvVaw0nT_e73Y8vpw2goqolBDCN)
* RMS Step by Step Tutorial - archived [here](https://www.google.com/url?q=https://web.archive.org/web/20101120092111/http:/dgdn.net/dgdn.php?id%3D3%26cat%3Darticle_pages%26heading_ID%3D1%26cat_ID%3D3&sa=D&source=editors&ust=1744981493714713&usg=AOvVaw0ktEwAOmzjcFrHbwKVENzX) and copied [here](https://www.google.com/url?q=http://www.yantri.net/aoe/rms.html&sa=D&source=editors&ust=1744981493714807&usg=AOvVaw0bTAFJ1Lu5OLWJdBrp-ISI)
* [How Connection Generation Really Works](https://www.google.com/url?q=https://web.archive.org/web/20010817031735/http:/www.crosswinds.net/~bryantighe/aok/howcon.html&sa=D&source=editors&ust=1744981493714984&usg=AOvVaw1zWhncP7oyBLKiXS1IOUx2) (archived)
* [RMS Mountain Making Tips](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D28,39054,30,all&sa=D&source=editors&ust=1744981493715150&usg=AOvVaw0z95Ih-7ug9EYfNd_V5Qde)
* Random Map Scripting Q & A by: Dr. Greg Street (ES\_Deathshrimp), Conquerors Lead Designer - archived [part 1](https://www.google.com/url?q=https://web.archive.org/web/20021205231557/http:/www.ensemblestudios.com/openjournal2/story/0905001739.shtml&sa=D&source=editors&ust=1744981493715394&usg=AOvVaw0cGOlCgzX-PJjHFkaTp3k4) and [part 2](https://www.google.com/url?q=https://web.archive.org/web/20021205231557/http:/www.ensemblestudios.com/openjournal2/story/0905001739.shtml&sa=D&source=editors&ust=1744981493715511&usg=AOvVaw13VJIZwpdIreMoO2BxYLnu)
* [More undocumented RM scripting commands](https://www.google.com/url?q=http://aok.heavengames.com/cgi-bin/forums/display.cgi?action%3Dct%26f%3D28,40974,,all&sa=D&source=editors&ust=1744981493715673&usg=AOvVaw39ksixcVEUk4TmnizWNf8j)
* [New RMS Guide](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D5792&sa=D&source=editors&ust=1744981493715805&usg=AOvVaw0kz2IhflMr5Openu0FeaPN) (outdated)
* [Updated New RMS Guide](https://www.google.com/url?q=http://aok.heavengames.com/blacksmith/showfile.php?fileid%3D12178&sa=D&source=editors&ust=1744981493715953&usg=AOvVaw1V-nq7ZVZ0C6N7wMj8aipx) (outdated, but still relevant for HD/UP1.4)

## Terrain Replacement Example Image

Using repeated terrain replacement to get rid of small terrain patches:

![](images/image13.jpg)

---

#

# RMS Effects in detail

This is a planned new chapter that will go into detail about the usage of [effect\_amount](#h.1niw1edwqhy5) and [effect\_percent](#h.7siepjsm3bdc) in modifying all of the possible [attributes](#h.oumcl095iabt), and provide examples.  For now, take a look at: [Attributes - AoE2DE UGC Guide](https://www.google.com/url?q=https://ugc.aoe2.rocks/general/attributes/attributes/&sa=D&source=editors&ust=1744981493716807&usg=AOvVaw3o1i87QNmSXOBO747-R5UY)

WORK IN PROGRESS

ATTR\_CREATE\_SDESC\_ID

[desired string ID] - 20000 to get the value you need

ATTR\_ATTACK

ATTR\_ARMOR

256\*class ID of the armor/attack you want to change
