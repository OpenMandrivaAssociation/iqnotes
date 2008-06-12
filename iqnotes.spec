%define	name    iqnotes
%define	version	2.1.0
%define	betaver	rc1
%define	release %mkrel 0.%betaver.1

%define	Summary Advanced outliner application

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Office
URL:		http://iqnotes.berlios.de/
Source0:	%name-%version%betaver.tar.bz2
Source1:	%name-icons.tar.bz2
Patch0:		%name.patch.bz2
BuildRoot:	%_tmppath/%name-%version-buildroot
Buildrequires:	libqt-devel

%description
IQNotes is notes kept in a hierarchical(tree like) manner. It handles todo,
events, sketching. It can acts as a contact, password, credit card manager and
even more, because is highly configurable. Data can be crypted by strong AES
algorithm.

%prep
%setup -q -n %{name}-%{version}%{betaver}
%setup -q -n %{name}-%{version}%{betaver} -T -D -a1
%patch

%build
QTDIR=%{_prefix}/lib/qt3
export QTDIR
cd %{name}
qmake
%make

%install
%__rm -rf %buildroot
%{__mkdir_p} %{buildroot}%{_prefix}
%{__install} -d %{buildroot}%{_bindir}
%{__install} bin/%{name} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__install} pics/%{name}/*.png %{buildroot}%{_datadir}/%{name}

# Menu
%__mkdir_p %buildroot%{_datadir}/applications
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application << EOF
Exec=%_bindir/%name
Icon=%name
Categories=Office;ProjectManagement
Name=IQNotes
Comment=%Summary
EOF

# icons
%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc %{name}/COPYING %{name}/COPYRIGHT %{name}/README.DESKTOP %{name}/INSTALL
%doc %{name}/ChangeLog %{name}/AUTHORS %{name}/THANKS %{name}/TODO
%{_datadir}/applications/mandriva-*.desktop
%dir %_datadir/%{name}
%_datadir/%{name}
%_miconsdir/*
%_iconsdir/*
%_liconsdir/*

