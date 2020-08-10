### set vagrant version
VAGRANTFILE_API_VERSION = "2"
VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

Vagrant::configure(VAGRANTFILE_API_VERSION) do |global_config|

  #use hostmanager plugin to configure /etc/hosts on host and guest
  global_config.hostmanager.enabled = true

  # begin host definition
  global_config.vm.define("jupyter.internal.tld") do |config|

    # use ubuntu image
    config.vm.box = "ubuntu/bionic64"

    # use hostmanager plugin to configure /etc/hosts
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    config.hostmanager.ignore_private_ip = false
    config.hostmanager.include_offline = true

    #configure private non-NAT interface
    config.vm.network :private_network, ip: "10.0.1.201"
    config.vm.hostname = "jupyter.internal.tld"

    #set virtual providor
    config.vm.provider "virtualbox" do |v|
        v.linked_clone = true
    end

    # bootstrap
    config.vm.provision "shell",
      inline: "apt-get update && apt-get -y upgrade"

    # provision
    config.vm.provision "ansible" do |ansible|
      ansible.verbose = "v"
      ansible.playbook = "./ansible/site.yml"
    end

  end
end
