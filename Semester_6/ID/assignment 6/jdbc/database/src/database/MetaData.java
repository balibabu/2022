package database;

import java.sql.SQLException;
import java.util.HashMap;

public class MetaData {
	HashMap<String, String> cols_dtype;

	public MetaData(String table) throws SQLException {
		cols_dtype = Query.columnsType("select * from " + table);
	}

}
