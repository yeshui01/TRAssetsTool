// this file created by gen_dbtable.py script at 2020-02-08 11:32:26

#ifndef __TB_ROLE_COIN_H__
#define __TB_ROLE_COIN_H__

// --------- custom code_1 begin --------
#include "testhfile.h"
// --------- custom code_1 end ----------

enum ETbRoleCoinField
{
	E_TB_ROLECOIN_FLD_ROLE_ID,
	E_TB_ROLECOIN_FLD_GOLD,
	E_TB_ROLECOIN_FLD_DIAMOND,
	E_TB_ROLECOIN_FLD_INITED,
	E_TB_%s_FLD_END
};

class TbRoleCoin : public DataTableBase
{
public:
	TbRoleCoin(int32_t table_id);
	~TbRoleCoin();
public:
	// role_id
	int64_t GetRoleId()
	{
		return GetFieldBigIntValue(E_TB_ROLECOIN_FLD_ROLE_ID)
	}
	int64_t GetRoleId() const
	{
		return GetFieldBigIntValue(E_TB_ROLECOIN_FLD_ROLE_ID)
	}
	void SetRoleId(int64_t role_id)
	{
		SetFieldBigIntValue(E_TB_ROLECOIN_FLD_ROLE_ID, role_id)
	}
	// gold
	int32_t GetGold()
	{
		return GetFieldIntValue(E_TB_ROLECOIN_FLD_GOLD)
	}
	int32_t GetGold() const
	{
		return GetFieldIntValue(E_TB_ROLECOIN_FLD_GOLD)
	}
	void SetGold(int32_t gold)
	{
		SetFieldIntValue(E_TB_ROLECOIN_FLD_GOLD, gold)
	}
	// diamond
	int32_t GetDiamond()
	{
		return GetFieldIntValue(E_TB_ROLECOIN_FLD_DIAMOND)
	}
	int32_t GetDiamond() const
	{
		return GetFieldIntValue(E_TB_ROLECOIN_FLD_DIAMOND)
	}
	void SetDiamond(int32_t diamond)
	{
		SetFieldIntValue(E_TB_ROLECOIN_FLD_DIAMOND, diamond)
	}
	// inited
	int32_t GetInited()
	{
		return GetFieldIntValue(E_TB_ROLECOIN_FLD_INITED)
	}
	int32_t GetInited() const
	{
		return GetFieldIntValue(E_TB_ROLECOIN_FLD_INITED)
	}
	void SetInited(int32_t inited)
	{
		SetFieldIntValue(E_TB_ROLECOIN_FLD_INITED, inited)
	}
// --------- custom code_2 begin --------
public:
    void GetCuctomVar();
protected:
    int32_t custom_var_ = 0;
// --------- custom code_2 end ----------
};

#endif // __TB_ROLE_COIN_H__