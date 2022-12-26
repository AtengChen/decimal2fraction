class float_to_fraction:
    def __init__(self, f):
        self.f = f
        self.process = ''

        self.process += 'set x = %s\n' % self.f

        length = len(str(self.f).split('.')[1])
        self.denominator = int('1' + length * '0')
        self.member = int(self.f * self.denominator)

        self.process += '%sx = %s\n' % (self.denominator, self.member)

        self.process += 'x = %s / %s\n' % (self.member, self.denominator)

        # 简化分母
        a, b = self.member, self.denominator
        while b != 0:
            temp = a % b
            a = b
            b = temp
        self.process += 'x = %s / %s\n' % (int(self.member / a), int(self.denominator / a))

        self.member = int(self.member / a)
        self.denominator = int(self.denominator / a)

    def __str__(self):
        return '%s / %s' % (self.member, self.denominator)


if __name__ == '__main__':
    f = float_to_fraction(float(input()))
    print(f)
    print()
    print(f.process)