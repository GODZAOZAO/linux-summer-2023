#include <stdint.h>
#include <stddef.h>
#include <stdio.h>

static inline uintptr_t align_up(uintptr_t sz, size_t alignment)
{
    uintptr_t mask = alignment - 1;
    if ((alignment & mask) == 0) {  /* power of two? */
        return (sz + mask) & ~mask;       
    }
    return (((sz + mask) / alignment) * alignment);
}

int main() {
    uintptr_t aligned_120 = align_up(120, 4);
    uintptr_t aligned_121 = align_up(121, 4);
    uintptr_t aligned_122 = align_up(122, 4);
    uintptr_t aligned_123 = align_up(123, 4);

    uintptr_t aligned_128 = align_up(128, 16);
    uintptr_t aligned_129 = align_up(129, 16);
    uintptr_t aligned_130 = align_up(130, 16);
    uintptr_t aligned_131 = align_up(131, 16);

    printf("align_up(120, 4) = %lu\n", aligned_120);
    printf("align_up(121, 4) = %lu\n", aligned_121);
    printf("align_up(122, 4) = %lu\n", aligned_122);
    printf("align_up(123, 4) = %lu\n", aligned_123);

    printf("align_up(128, 16) = %lu\n", aligned_128);
    printf("align_up(129, 16) = %lu\n", aligned_129);
    printf("align_up(130, 16) = %lu\n", aligned_130);
    printf("align_up(131, 16) = %lu\n", aligned_131);
    
    return 0;
}