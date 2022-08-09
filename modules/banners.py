from log import println, colours, warning, info
from platform import system as system_name

if system_name() == "Windows":
    from colourama import init
    init()


def print_banner():
    banner = """
    ___       ____       ___       ___       _  _       ____       ___      _  _   
   F __".    F ___J    ,"___".   ,"___".    FJ  L]     F ___J    ,"___".   FJ / ;  
  J (___|   J |___:    FJ---L]   FJ---L]   J |__| L   J |___:    FJ---L]  J |/ (|  
  J\___ \   | _____|  J |   LJ  J |   LJ   |  __  |   | _____|  J |   LJ  |     L  
 .--___) \  F L____:  | \___--. | \___--.  F L__J J   F L____:  | \___--. F L:\  L 
 J\______J J________L J\_____/F J\_____/F J__L  J__L J________L J\_____/FJ__L \\__L
  J______F |________|  J_____F   J_____F  |__L  J__| |________|  J_____F |__L  \L_|"""
                                                                                   
    print()
    info("The Sanity Checking Configuration program for network/server security.")
    println("\n" + "┌" + "─" * 88 + "┐")
    println(banner.center(90))
    println("└" + "─" * 88 + "┘" + "\n")

