    # ejercicio 4
def towersOfHanoi(nro_disks, from_tower=1, to_tower=3, aux_tower=2):
    if nro_disks == 1:
        print(f"Mover el disco {nro_disks} desde la torre {from_tower} a la torre {to_tower}")
        return
    towersOfHanoi(nro_disks - 1, from_tower, aux_tower, to_tower)
    print(f"Mover el disco {nro_disks} desde la torre {from_tower} a la torre {to_tower}")
    towersOfHanoi(nro_disks - 1, aux_tower, to_tower, from_tower)
if __name__ == "__main__":
    towersOfHanoi(nro_disks=3)

