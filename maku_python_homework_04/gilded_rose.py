# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            operator = get_class_operator(item)
            operator.update()

    def update_quality_old(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


def get_class_operator(item):
    if item.name == "Aged Brie":
        return UpdateAgedbrie(item)
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return UpdateBackstage(item)
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return UpdateSulfuras(item)
    else:
        return UpdateEasy(item)


class UpdateBase:
    def __init__(self, item):
        self.item = item
    
    def update(self):
        self.update_quality()
        self.update_sellin()
        if self.item.sell_in < 0:
            self.update_quality_passed()
    
    def update_quality(self):
        raise NotImplementedError
    
    def update_sellin(self):
        raise NotImplementedError

    def update_quality_passed(self):
        raise NotImplementedError


class UpdateEasy(UpdateBase):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def update_sellin(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality_passed(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1
    
class UpdateAgedbrie(UpdateBase):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1
    
    def update_sellin(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality_passed(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1


class UpdateBackstage(UpdateBase):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

            if self.item.sell_in <= 10:
                self.item.quality += 1
            
            if self.item.sell_in <= 5:
                self.item.quality += 1

    def update_quality_passed(self):
        self.item.quality = 0


class UpdateSulfuras(UpdateBase):
    def update_quality(self):
        self.item.quality = self.item.quality

    def update_quality_passed(self):
        self.item.quality = self.item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
