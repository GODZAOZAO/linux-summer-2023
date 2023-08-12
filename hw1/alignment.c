#include <stdint.h>
#include <stddef.h>

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
    
    printf("align_up(120, 4) = %lu\n", aligned_120);
    printf("align_up(121, 4) = %lu\n", aligned_121);
    printf("align_up(122, 4) = %lu\n", aligned_122);
    printf("align_up(123, 4) = %lu\n", aligned_123);
    
    return 0;
}