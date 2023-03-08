from selene import have


class Checkbox:
    def __init__(self, element):
        self.element = element

    def select(self, by_texts):
        self.element.element_by(have.text(by_texts)).click()