class Parent:
    def properties(self):
        self.props={"mobile":"nokia","bike":"passion pro"}
        return self.props

class Child(Parent):
    def properties(self):
        props= super().properties()
        props["car"]="swfit"
        return props

ch= Child()
print(ch.properties())

# super-> refer parent class
