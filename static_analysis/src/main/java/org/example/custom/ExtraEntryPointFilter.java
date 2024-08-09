package org.example.custom;

import soot.toolkits.scalar.Pair;

public interface ExtraEntryPointFilter {
	public boolean shouldIgnoreEntryPoint(Pair<String, String> entry);
}
