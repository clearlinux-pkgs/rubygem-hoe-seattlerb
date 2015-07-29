#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hoe-seattlerb
Version  : 1.3.4
Release  : 2
URL      : https://rubygems.org/downloads/hoe-seattlerb-1.3.4.gem
Source0  : https://rubygems.org/downloads/hoe-seattlerb-1.3.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= hoe-seattlerb
home :: https://github.com/seattlerb/hoe-seattlerb
rdoc :: http://seattlerb.rubyforge.org/hoe-seattlerb

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hoe-seattlerb-1.3.4
gem spec %{SOURCE0} -l --ruby > rubygem-hoe-seattlerb.gemspec

%build
gem build rubygem-hoe-seattlerb.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hoe-seattlerb-1.3.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/hoe-seattlerb-1.3.4
rake --trace test TESTOPTS="-v"
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/hoe-seattlerb-1.3.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Email/cdesc-Email.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Email/define_email_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Email/email_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Email/initialize_email-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/History/cdesc-History.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/History/flog_flay-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/History/history-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/History/load_history-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/History/save_history-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/cdesc-Perforce.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/define_perforce_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/initialize_perforce-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/p4_history-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/p4_integrate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/p4_revert-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/p4_submit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/p4_versions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/p4sh-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/perforce_ignore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Perforce/validate_manifest_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Seattlerb/cdesc-Seattlerb.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/Seattlerb/define_seattlerb_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/Hoe/cdesc-Hoe.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-seattlerb-1.3.4/ri/page-README_txt.ri
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/README.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/lib/hoe/email.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/lib/hoe/history.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/lib/hoe/perforce.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-seattlerb-1.3.4/lib/hoe/seattlerb.rb
/usr/lib64/ruby/gems/2.2.0/specifications/hoe-seattlerb-1.3.4.gemspec
