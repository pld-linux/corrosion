#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.27
%define		qtver		5.15.2
%define		kfname		kidletime

Summary:	Integrate Rust into CMake projects
Name:		corrosion
Version:	0.6.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/corrosion-rs/corrosion/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	060ee79a6bf7c5a2e4e810370fbb7b61
URL:		http://www.kde.org/
BuildRequires:	cmake >= 3.22
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Corrosion, formerly known as cmake-cargo, is a tool for integrating
Rust into an existing CMake project.

%description -l pl.UTF-8
Corrosion, poprzednio znany jako cmake-cargo, jest narzędziem do
integracji Rusta z istniejącymi projektami CMake.

%prep
%setup -q

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_libdir}/cmake/Corrosion/CorrosionConfig.cmake
%{_libdir}/cmake/Corrosion/CorrosionConfigVersion.cmake
%{_datadir}/cmake/Corrosion.cmake
%{_datadir}/cmake/CorrosionGenerator.cmake
%{_datadir}/cmake/FindRust.cmake
