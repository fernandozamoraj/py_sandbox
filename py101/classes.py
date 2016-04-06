class JobRunner:
    def run(self):
        print "Job Runner Running"
		
class PrintRunner: 
    def run(self):
        print "PrintRunner running"

#inheritance only for sharing common functionality
class Vehicle:
    def __init__(self, wheels):        
        self._wheels = wheels
        
    def wheels(self):
        return self._wheels
        
class Bike(Vehicle):
    def model(self):
        return "Bike"
        
class Auto(Vehicle):
    def model(self):
        return "Auto"

#notice there is no relationship between print runner and job runner
#other than that they both implement run	
#this is an example of duck typing
def run(runner):
    runner.run()

run(JobRunner())
run(PrintRunner())
	
bike = Bike(2)
auto = Auto(4)

print "bike has {0} wheels".format(bike.wheels())
print "auto has {0} wheels".format(auto.wheels())

    