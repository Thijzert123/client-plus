#!/bin/bash

export IFS=" "

mods="yosbr moreculling modmenu iris dynamic-fps sodium morechathistory capes zoomify ferrite-core sodium-extra immediatelyfast language-reload lambdynamiclights badoptimizations vmp-fabric entity-model-features entitytexturefeatures lighty better-stats music-notification status-effect-bars mace-but-3d glowing-torchflower detail-armor-bar visuality simple-voice-chat chat-heads mouse-tweaks clientsort bobby fastquit no-chat-reports mixintrace e4mc modelfix entityculling fabrishot controlify lithium appleskin modernfix cubes-without-borders better-mount-hud ebe continuity fabricskyboxes fabricskyboxes-interop noisium litematica shulkerboxtooltip betterf3 eating-animation pick-up-notifier cherished-worlds polytone world-play-time skinshuffle no-resource-pack-warnings infinite-music particular 3dskinlayers auth-me inventory-blur calcmod chunky noemotecraft better-f1-reborn xaeros-world-map xaeros-minimap not-enough-animations fast-ip-ping extended-world-selection clumps legendary-tooltips"

shaders="makeup-ultra-fast-shaders miniature-shader solas-shader rethinking-voxels complementary-unbound bsl-shaders complementary-reimagined"

resources="default-splashes fullbright-ub fresh-animations visual-armor-trims icons better-flame-particles simple-grass-flowers mob-crates fancy-crops qraftys-capitalized-font enchant-icons-countxd even-better-enchants cubic-sun-moon redstone-tweaks low-on-fire fresh-player-animations better-leaves 3d-plants spectral reimagined hyper-realistic-sky grimdark-sky animated-items better-lanterns"

for mod in $mods
do
    packwiz modrinth install $mod -y
done

for shader in $shaders
do
    packwiz modrinth install $shader -y
done

for resource in $resources
do
    packwiz modrinth install $resource -y
done