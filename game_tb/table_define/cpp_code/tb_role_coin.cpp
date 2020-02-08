// this file created by gen_dbtable.py script at 2020-02-08 11:32:26

#include "tb_role_coin.h"

// --------- custom code_3 begin --------
#include "custom_hfile.h"
// --------- custom code_3 end ----------

TbRoleCoin::TbRoleCoin(int32_t table_id) : DataTableBase(table_id)
{
	// role_id
	AddField(E_FIELD_VALUE_TYPE_BIG_INT, true);
	// gold
	AddField(E_FIELD_VALUE_TYPE_INT, false);
	// diamond
	AddField(E_FIELD_VALUE_TYPE_INT, false);
	// inited
	AddField(E_FIELD_VALUE_TYPE_INT, false);
}
TbRoleCoin::~TbRoleCoin()
{
}
// --------- custom code_4 begin --------
void TbRoleCoin::GetCuctomVar()
{
    return custom_var_;
}
// --------- custom code_4 end ----------

