class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None

    def __str__(self):
        return f"Computer with CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}GB"

class ComputerBuilder:
    def reset(self):
        raise NotImplementedError()
    def set_cpu(self):
        raise NotImplementedError()
    def set_gpu(self):
        raise NotImplementedError()
    def set_ram(self):
        raise NotImplementedError()

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()
    def reset(self):
        self.computer = Computer()
    def set_cpu(self):
        self.computer.cpu = "Intel Core i9"
        return self
    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 3090"
        return self
    def set_ram(self):
        self.computer.ram = 32
        return self
    def get_result(self):
        return self.computer

class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()
    def reset(self):
        self.computer = Computer()
    def set_cpu(self):
        self.computer.cpu = "Intel Core i5"
        return self
    def set_gpu(self):
        self.computer.gpu = "Integrated"
        return self
    def set_ram(self):
        self.computer.ram = 8
        return self
    def get_result(self):
        return self.computer


class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    def build_gaming_computer(self):
        self.builder.reset()
        self.builder.set_cpu().set_gpu().set_ram()
        return self.builder.get_result()
    def build_office_computer(self):
        self.builder.reset()
        self.builder.set_cpu().set_gpu().set_ram()
        return self.builder.get_result()


gaming_builder = GamingComputerBuilder()
office_builder = OfficeComputerBuilder()
director = Director(gaming_builder)
gaming_computer = director.build_gaming_computer()
print(gaming_computer)
director = Director(office_builder)
office_computer = director.build_office_computer()
print(office_computer)
