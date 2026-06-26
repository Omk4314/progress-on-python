class Browser:
    def __init__(self):
        self.pointer = -1
        self.history = []

    def forward(self):
        if self.pointer == -1:
            print("No history found")
            return None
        if self.pointer >= len(self.history) - 1:
            print("Can't go forward!")
            return None
        self.pointer += 1
        return self.history[self.pointer]

    def backward(self):
        if self.pointer == -1:
            print("No history found")
            return None
        if self.pointer == 0:
            print("Can't go back!")
            return None
        self.pointer -= 1
        return self.history[self.pointer]

    def visit_site(self, site_name):
        # Cut off future history, keep current page
        if self.pointer != -1:
            self.history = self.history[:self.pointer + 1]
        self.history.append(site_name)
        self.pointer = len(self.history) - 1
        return self.history

    def show_history(self):
        if not self.history:
            print("No history found!")
            return
        for i, site in enumerate(self.history):
            marker = "  <-- current" if i == self.pointer else ""
            print(f"  {site}{marker}")

def test():
    print("=" * 50)
    print("TEST 1: Empty browser")
    print("=" * 50)
    b = Browser()
    b.show_history()
    print(f"Forward: {b.forward()}")
    print(f"Backward: {b.backward()}")

    print("\n" + "=" * 50)
    print("TEST 2: Visit 3 sites")
    print("=" * 50)
    b = Browser()
    b.visit_site("google.com")
    b.visit_site("github.com")
    b.visit_site("stackoverflow.com")
    b.show_history()

    print("\n" + "=" * 50)
    print("TEST 3: Go back twice")
    print("=" * 50)
    b = Browser()
    b.visit_site("google.com")
    b.visit_site("github.com")
    b.visit_site("stackoverflow.com")
    print(f"Start: pointer = {b.pointer}")
    print(f"Back: {b.backward()}")
    print(f"Back: {b.backward()}")
    print(f"Pointer now: {b.pointer}")
    b.backward()  # Should fail

    print("\n" + "=" * 50)
    print("TEST 4: Go forward")
    print("=" * 50)
    b = Browser()
    b.visit_site("google.com")
    b.visit_site("github.com")
    b.visit_site("stackoverflow.com")
    b.backward()
    b.backward()
    print(f"After 2 back: pointer = {b.pointer}")
    print(f"Forward: {b.forward()}")
    print(f"Forward: {b.forward()}")
    b.forward()  # Should fail

    print("\n" + "=" * 50)
    print("TEST 5: Visit new site after going back (truncate future)")
    print("=" * 50)
    b = Browser()
    b.visit_site("google.com")
    b.visit_site("github.com")
    b.visit_site("stackoverflow.com")
    b.backward()
    b.backward()
    print("Before visiting reddit:")
    b.show_history()
    b.visit_site("reddit.com")
    print("After visiting reddit:")
    b.show_history()
    b.forward()  # Should fail - no future

    print("\n" + "=" * 50)
    print("TEST 6: Duplicate site names")
    print("=" * 50)
    b = Browser()
    b.visit_site("google.com")
    b.visit_site("yahoo.com")
    b.visit_site("google.com")
    b.show_history()

    print("\n" + "=" * 50)
    print("TEST 7: Single page - edge cases")
    print("=" * 50)
    b = Browser()
    b.visit_site("only-site.com")
    b.backward()  # Fail
    b.forward()   # Fail
    b.show_history()

    print("\n" + "=" * 50)
    print("TEST 8: Back then forward then back again")
    print("=" * 50)
    b = Browser()
    b.visit_site("A")
    b.visit_site("B")
    b.visit_site("C")
    b.backward()
    b.backward()
    b.forward()
    print(f"After A->B->C, back, back, forward: pointer = {b.pointer}")
    b.show_history()
    b.backward()
    print(f"After another back: pointer = {b.pointer}")
    b.show_history()


if __name__ == "__main__":
    test()