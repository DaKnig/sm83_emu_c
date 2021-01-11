
%.o: %.c
	$(CC) -c -o $@ $<
cpu.c: cpu.c.cog instr_processor.py
	cog -o $@ $<

clean:
	rm -f cpu.c *.o
