from abc import ABC, abstractmethod

class RemoteControl:
    def __init__(self, device):
        self._device = device #Device is going be used as class

    def togglePower(self):
        if self._device.isEnabled == "On":
            self._device.disable()
        else:
            self._device.enable() 

    def volumeDown(self):
        self._device.setVolume(self._device.getVolume() - 10)

    def volumeUp(self):
        self._device.setVolume(self._device.getVolume() + 10)

    def channelDown(self):
        self._device.setChannel(self._device.getChannel() - 1)

    def channelUp(self):
        self._device.setChannel(self._device.getChannel() + 1)

class AdvancedRemoteControl(RemoteControl):

    def mute(self):
        self._device.setVolume(0)


class Device:
    @abstractmethod
    def isEnabled():
        pass

    @abstractmethod
    def enable():
        pass

    @abstractmethod
    def disable():
        pass

    @abstractmethod
    def getVolume():
        pass

    @abstractmethod
    def setVolume():
        pass

    @abstractmethod
    def getChannel():
        pass

    @abstractmethod
    def setChannel():
        pass

class TV(Device):

    def __init__(self):
        self.status = 'On'
        self.volume = int(10)
        self.channel = int(1)

    def isEnabled(self):
        if self.status == 'On':
            return "TV has been turned on!" 

    def enable(self):
        if self.status == 'On':
            return "TV is already turned on!"
        else:
            self.status == 'On'
            return "TV will be turning on!"

    def disable(self):
        if self.status == 'Off':
            return "TV is already turned off!"
        else:
            self.status == 'Off'
            return "TV will be turning on!"

    def getVolume(self) -> int:
        return self.volume

    def setVolume(self, new_volume):
        self.volume = new_volume
        return f'The new volume is {self.volume}'

    def getChannel(self):
        return self.channel

    def setChannel(self, new_channel):
        self.channel = new_channel
        return f'The new channel is {self.channel}'
        

class Radio(Device):

    name = 'Radio'
    
    def __init__(self):
        self.status = 'On'
        self.volume = int(10)
        self.channel = int(1)

    def isEnabled(self):
        if self.status == 'On':
            print(f"{Radio.name} has been turned on!")

    def enable(self):
        if self.status == 'On':
            print(f"{Radio.name} is already turned on!")
        else:
            self.status == 'On'
            print(f"{Radio.name} will be turning on!")

    def disable(self):
        if self.status == 'Off':
            print(f"{Radio.name}is already turned off!")
        else:
            self.status == 'Off'
            print(f"{Radio.name} will be turning on!")

    def getVolume(self) -> int:
        return self.volume

    def setVolume(self, new_volume):
        self.volume = new_volume
        print(f'The new volume is {self.volume}')

    def getChannel(self):
        return self.channel

    def setChannel(self, new_channel):
        self.channel = new_channel
        print(f'The new channel is {self.channel}')

def main():
    tv = TV()
    remote = RemoteControl(tv)
    remote.togglePower()

    radio = Radio()
    remote = AdvancedRemoteControl(radio)
    remote.togglePower()
    remote.volumeUp()
    remote.volumeDown()


#In the unit test below, we are going to toggle between different forms of power. 

main()