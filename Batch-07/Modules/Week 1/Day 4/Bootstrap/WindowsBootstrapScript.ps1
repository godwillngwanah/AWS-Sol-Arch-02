<powershell>
Start-Transcript;

# Install IIS
Import-Module ServerManager;
Enable-WindowsOptionalFeature   -Online	-NoRestart	-FeatureName	'IIS-  WebServerRole', 'IIS-WebServer', 'IIS-ManagementConsole';
</powershell>
