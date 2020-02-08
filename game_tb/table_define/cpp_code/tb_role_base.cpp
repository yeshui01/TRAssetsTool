// this file created by gen_dbtable.py script at 2020-02-07 19:19:23

#include "tb_role_base.h"

// --------- custom code_3 begin --------
// --------- custom code_3 end --------

TbRoleBase::TbRoleBase(int32_t table_id) : DataTableBase(table_id)
{
	// role_id
	AddField(E_FIELD_VALUE_TYPE_BIG_INT, true);
	// acc_id
	AddField(E_FIELD_VALUE_TYPE_BIG_INT, false);
	// nickname
	AddField(E_FIELD_VALUE_TYPE_STRING, false);
	// crate_time
	AddField(E_FIELD_VALUE_TYPE_BIG_INT, false);
	// zone_id
	AddField(E_FIELD_VALUE_TYPE_INT, false);
	// inited
	AddField(E_FIELD_VALUE_TYPE_INT, false);
}
TbRoleBase::~TbRoleBase()
{
}
// --------- custom code_4 begin --------
// --------- custom code_4 end --------

