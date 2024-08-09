package org.example.custom;

import soot.jimple.Stmt;

public interface ExtraSourceFilter {
	public boolean shouldIgnoreSource(Stmt stmt, String hostClazzName);
}
