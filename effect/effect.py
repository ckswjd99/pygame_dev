import particle
import numpy

whole = []
kill_MOUSEBUTTONUP = []



#---------- Root Class: effect ----------#

class effect:
    def __init__(self, pos):
        self.particles = []
        self.pos = pos
        whole.append(self)

    def update(self):
        for p in self.particles:
            p.update()
        pass

    def render(self):
        for p in self.particles:
            p.render()
        pass

    def demol(self):
        whole.remove(self)
        pass



#---------- Children Class: SPARKS ----------#

class spark_circle(effect):
    def __init__(self, pos, life, speed, size, color, num):
        effect.__init__(self, pos)
        for i in range(num):
            angle = numpy.random.rand()*2
            particle.spark_circle(self, pos, life, speed, angle, size, color)

    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()

class spark_rectangle(effect):
    def __init__(self, pos, life, speed, size, color, num):
        effect.__init__(self, pos)
        for i in range(num):
            angle = numpy.random.rand()*2
            particle.spark_rectangle(self, pos, life, speed, angle, size, color)

    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()



#---------- Children Class: SPARKS with gravity ----------#

class spark_gravity_circle(effect):
    def __init__(self, pos, life, gravity, speed, size, color, num):
        effect.__init__(self, pos)
        for i in range(num):
            angle = numpy.random.rand()*2
            particle.spark_gravity_circle(self, pos, life, gravity, speed, angle, size, color)

    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()

class spark_gravity_rectangle(effect):
    def __init__(self, pos, life, gravity, speed, size, color, num):
        effect.__init__(self, pos)
        for i in range(num):
            angle = numpy.random.rand()*2
            particle.spark_gravity_rectangle(self, pos, life, gravity, speed, angle, size, color)

    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()



#---------- Children Class: FOUNTAIN ----------#

class fountain_circle(effect):
    def __init__(self, pos, life, delay, speed, size, color, num, kill_when):
        effect.__init__(self, pos)
        self.life = life
        self.delay = delay
        self.delay_now = 0
        self.speed = speed
        self.size = size
        self.color = color
        self.num = num
        self.generate = True

        kill_when.append(self)

    def update(self):
        for p in self.particles:
            p.update()
        if self.delay_now == 0 and self.generate == True:
            for i in range(self.num):
                angle = numpy.random.rand()*2
                particle.spark_circle(self, self.pos, self.life, self.speed, angle, self.size, self.color)
            self.delay_now = self.delay
        else:
            self.delay_now -= 1
        if self.particles == []:
            self.demol()

    def kill(self):
        self.generate = False;

class fountain_rectangle(effect):
    def __init__(self, pos, life, delay, speed, size, color, num, kill_when):
        effect.__init__(self, pos)
        self.life = life
        self.delay = delay
        self.delay_now = 0
        self.speed = speed
        self.size = size
        self.color = color
        self.num = num
        self.generate = True

        kill_when.append(self)

    def update(self):
        for p in self.particles:
            p.update()
        if self.delay_now == 0 and self.generate == True:
            for i in range(self.num):
                angle = numpy.random.rand()*2
                particle.spark_rectangle(self, self.pos, self.life, self.speed, angle, self.size, self.color)
            self.delay_now = self.delay
        else:
            self.delay_now -= 1
        if self.particles == []:
            self.demol()

    def kill(self):
        self.generate = False;



#---------- Children Class: FOUNTAIN with gravity ----------#

class fountain_gravity_circle(effect):
    def __init__(self, pos, life, gravity, delay, speed, size, color, num, kill_when):
        effect.__init__(self, pos)
        self.life = life
        self.gravity = gravity
        self.delay = delay
        self.delay_now = 0
        self.speed = speed
        self.size = size
        self.color = color
        self.num = num
        self.generate = True

        kill_when.append(self)

    def update(self):
        for p in self.particles:
            p.update()
        if self.delay_now == 0 and self.generate == True:
            for i in range(self.num):
                angle = numpy.random.rand()*2
                particle.spark_gravity_circle(self, self.pos, self.life, self.gravity, self.speed, angle, self.size, self.color)
            self.delay_now = self.delay
        else:
            self.delay_now -= 1
        if self.particles == []:
            self.demol()

    def kill(self):
        self.generate = False;

class fountain_gravity_rectangle(effect):
    def __init__(self, pos, life, gravity, delay, speed, size, color, num, kill_when):
        effect.__init__(self, pos)
        self.life = life
        self.gravity = gravity
        self.delay = delay
        self.delay_now = 0
        self.speed = speed
        self.size = size
        self.color = color
        self.num = num
        self.generate = True

        kill_when.append(self)

    def update(self):
        for p in self.particles:
            p.update()
        if self.delay_now == 0 and self.generate == True:
            for i in range(self.num):
                angle = numpy.random.rand()*2
                particle.spark_gravity_rectangle(self, self.pos, self.life, self.gravity, self.speed, angle, self.size, self.color)
            self.delay_now = self.delay
        else:
            self.delay_now -= 1
        if self.particles == []:
            self.demol()

    def kill(self):
        self.generate = False;



#---------- Children Class: WAVE ----------#

class wave_circle(effect):
    def __init__(self, pos, life, speed, size, color):
        effect.__init__(self, pos)
        particle.wave_circle(self, pos, life, speed, size, color)

    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()    

class wave_rectangle(effect):
    def __init__(self, pos, life, speed, size, color):
        effect.__init__(self, pos)
        particle.wave_rectangle(self, pos, life, speed, size, color)

    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()



#---------- Children Class: GAS ----------#

class gas_circle(effect):
    def __init__(self, pos, life, speed, size, color, num):
        effect.__init__(self, pos)
        for i in range(num):
            angle = numpy.random.rand()*0.5 - 0.25
            particle.gas_circle(self, pos, life, speed, angle, size, color)
    
    def update(self):
        for p in self.particles:
            p.update()
        if self.particles == []:
            self.demol()

