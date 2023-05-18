# Photoshop CC 2021 for Linux
Initial script [here](https://github.com/LinSoftWin/Photoshop-CC2022-Linux)

## Requirements:
- [Wine 7.22](https://archive.archlinux.org/packages/w/wine/wine-7.22-1-x86_64.pkg.tar.zst) (thanks to [this comment](https://github.com/LinSoftWin/Photoshop-CC2022-Linux/issues/94#issuecomment-1426776219))
- The Samba package
- The ones listed [here](https://github.com/LinSoftWin/Photoshop-CC2022-Linux#requirements)

## Files to download:
- https://drive.google.com/uc?export=download&id=1qcmyHzWerZ39OhW0y4VQ-hOy7639bJPO (rename to allredist.tar.xz)

- https://lulucloud.mywire.org/FileHosting/GithubProjects/AdobePhotoshop2021.tar.xz (rename to AdobePhotoshop2021.tar.xz)

## Files setup:
- Make the /home/nix/ps/ folder
- Move the 2 files downloaded above into it
- Move the installer script & the winetricks files into it
- Extract wine 7.22 in it (so that you have /home/nix/ps/usr/bin/wine)

Now just launch the installer script & you should be done !


## Additional info
### First startup
Go to edit>preferences>performances, under "detected graphics processor" you should see your GPU name. If it isn't there, there was a problem w the installation. Make sure you're on wine 7.22 as wine 8 has issues with this.

### Changed winetricks lines:
- 5362
- 5367

To not destroy my github language usage stats, the file's been deleted from here.

Get it [from the commit history](https://github.com/Nixuge/RandomScripts/blob/d034032cb04bfe005d23af4dc6b67b791c5a6493/PhotoshopCC2021Linux/winetricks)

Or from pastebin: login to Google, then combine https://pastebin.com/Fwra1XRa and https://pastebin.com/194AcvUA
