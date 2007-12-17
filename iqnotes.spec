%define	name    iqnotes
%define	version	2.1.0
%define	betaver	rc1
%define	release %mkrel 0.%betaver.1

%define	section	Office/Tasks Management
%define	title   IQNotes

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
%__mkdir_p %buildroot%_menudir
cat > %buildroot%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="X11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%Summary"
EOF

# icons
%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc %{name}/COPYING %{name}/COPYRIGHT %{name}/README.DESKTOP %{name}/INSTALL
%doc %{name}/ChangeLog %{name}/AUTHORS %{name}/THANKS %{name}/TODO
%_menudir/*
%dir %_datadir/%{name}
%_datadir/%{name}
%_miconsdir/*
%_iconsdir/*
%_liconsdir/*

