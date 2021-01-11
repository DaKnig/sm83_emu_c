/*
  this is a declaration of the CPU emulator for the game boy
*/

#include <stdint.h>

// copied from SameBoy
#if __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__
#define GB_BIG_ENDIAN
#elif __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
#define GB_LITTLE_ENDIAN
#else
#error Unable to detect endianess
#endif

union regs{
    uint16_t registers[5];
    struct {
        uint16_t af,
                 bc,
                 de,
                 hl,
                 sp,
                 pc;
    };
    struct {
#ifdef GB_BIG_ENDIAN
        uint8_t a, f,
                b, c,
	        d, e,
                h, l;
#else
        uint8_t f, a,
                c, b,
                e, d,
                l, h;
#endif
    };
};

struct SM83 {
    union regs regs;
    uint8_t mem[1<<16]; // assume the whole memory map is RAM for simplicity
};

