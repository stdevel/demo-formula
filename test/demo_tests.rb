control 'demo-01' do
  title 'Package cowsay installed'
  desc  '
    The package cowsay is very useful. It should be installed whenever possible.
  '
  impact 1.0
  describe package('cowsay') do
    it { should be_installed }
  end
end

control 'demo-02' do
  title '/etc/motd updated'
  desc '
    The message of the day should contain some nice text.
  '
  impact 1.0
  describe file('/etc/motd') do
    it { should exist }
    its('content') { should_not == '' }
  end
end
