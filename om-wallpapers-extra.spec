Summary:	Collection of wallpapers provided by OpenMandriva users
Name:		om-wallpapers-extra
Version:	1
Release:	ZED'S DEAD BABY
License:	GPL
Group:		Graphics
Url:		https://www.openmandriva.org
# Source backup available here: https://github.com/rugyada/om-wallpapers-extra
Source0:	Energy_Grid.jpg
Source1:	Energy_Rays-at-sunset.jpg
Source2:	Energy_The-sunset.jpg
Source3:	Energy_Whiterays.jpg
Source4:	Flavor_of_freedom_Cantaloupe_Island.jpg
Source5:	Flavor_of_freedom_Dantes_Skyline.jpg
Source6:	Flavor_of_freedom_Descartes_Awakening.jpg
Source7:	Flavor_of_freedom_Glacier.jpg
Source8:	Flavor_of_freedom_Kampenwand.jpg
Source9:	Flavor_of_freedom_Lake_walen.jpg
Source10:	Flavor_of_freedom_Misty_Mountains.png
Source11:	Flavor_of_freedom_Mythen.jpg
Source12:	Flavor_of_freedom_Pastures.jpg
Source13:	Flavor_of_freedom_Reflection2.jpg
Source14:	The-atmosphere_Maquapit-Lake.png
Source15:	The-atmosphere_Nitro1.jpg
Source16:	The-atmosphere_Nitrogen01.png
Source17:	The-atmosphere_NitrogenC.jpg
Source18:	The-atmosphere_Nitrogen-OM.jpg
Source19:	The-atmosphere_Sky-View.jpg
BuildArch:	noarch

%description
Collection of wallpapers provided by OpenMandriva users

%files
%{_datadir}/wallpapers/om-wallpapers-extra

#----------------------------------------------------------------------------

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/wallpapers/om-wallpapers-extra
install -c -m 644 \
	%{S:0} \
	%{S:1} \
	%{S:2} \
	%{S:3} \
	%{S:4} \
	%{S:5} \
	%{S:6} \
	%{S:7} \
	%{S:8} \
	%{S:9} \
	%{S:10} \
	%{S:11} \
	%{S:12} \
	%{S:13} \
	%{S:14} \
	%{S:15} \
	%{S:16} \
	%{S:17} \
	%{S:18} \
	%{S:19} \
	%{buildroot}%{_datadir}/wallpapers/om-wallpapers-extra/
