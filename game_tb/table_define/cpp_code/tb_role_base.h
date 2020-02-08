// this file created by gen_dbtable.py script at 2020-02-07 19:19:23

#ifndef __TB_ROLE_BASE_H__
#define __TB_ROLE_BASE_H__

// --------- custom code_1 begin --------
// --------- custom code_1 end --------

enum ETbRoleBaseField
{
	E_TB_ROLEBASE_FLD_ROLE_ID,
	E_TB_ROLEBASE_FLD_ACC_ID,
	E_TB_ROLEBASE_FLD_NICKNAME,
	E_TB_ROLEBASE_FLD_CRATE_TIME,
	E_TB_ROLEBASE_FLD_ZONE_ID,
	E_TB_ROLEBASE_FLD_INITED,
	E_TB_%s_FLD_END
};

class TbRoleBase : public DataTableBase
{
public:
	TbRoleBase(int32_t table_id);
	~TbRoleBase();
public:
	// role_id
	int64_t GetRoleId()
	{
		return GetFieldBigIntValue(E_TB_ROLEBASE_FLD_ROLE_ID)
	}
	int64_t GetRoleId() const
	{
		return GetFieldBigIntValue(E_TB_ROLEBASE_FLD_ROLE_ID)
	}
	void SetRoleId(int64_t role_id)
	{
		SetFieldBigIntValue(E_TB_ROLEBASE_FLD_ROLE_ID, role_id)
	}
	// acc_id
	int64_t GetAccId()
	{
		return GetFieldBigIntValue(E_TB_ROLEBASE_FLD_ACC_ID)
	}
	int64_t GetAccId() const
	{
		return GetFieldBigIntValue(E_TB_ROLEBASE_FLD_ACC_ID)
	}
	void SetAccId(int64_t acc_id)
	{
		SetFieldBigIntValue(E_TB_ROLEBASE_FLD_ACC_ID, acc_id)
	}
	// nickname
	std::string GetNickname()
	{
		return GetFieldStringValue(E_TB_ROLEBASE_FLD_NICKNAME)
	}
	std::string GetNickname() const
	{
		return GetFieldStringValue(E_TB_ROLEBASE_FLD_NICKNAME)
	}
	void SetNickname(std::string nickname)
	{
		SetFieldStringValue(E_TB_ROLEBASE_FLD_NICKNAME, nickname.c_str(), nickname.size())
	}
	// crate_time
	int64_t GetCrateTime()
	{
		return GetFieldBigIntValue(E_TB_ROLEBASE_FLD_CRATE_TIME)
	}
	int64_t GetCrateTime() const
	{
		return GetFieldBigIntValue(E_TB_ROLEBASE_FLD_CRATE_TIME)
	}
	void SetCrateTime(int64_t crate_time)
	{
		SetFieldBigIntValue(E_TB_ROLEBASE_FLD_CRATE_TIME, crate_time)
	}
	// zone_id
	int32_t GetZoneId()
	{
		return GetFieldIntValue(E_TB_ROLEBASE_FLD_ZONE_ID)
	}
	int32_t GetZoneId() const
	{
		return GetFieldIntValue(E_TB_ROLEBASE_FLD_ZONE_ID)
	}
	void SetZoneId(int32_t zone_id)
	{
		SetFieldIntValue(E_TB_ROLEBASE_FLD_ZONE_ID, zone_id)
	}
	// inited
	int32_t GetInited()
	{
		return GetFieldIntValue(E_TB_ROLEBASE_FLD_INITED)
	}
	int32_t GetInited() const
	{
		return GetFieldIntValue(E_TB_ROLEBASE_FLD_INITED)
	}
	void SetInited(int32_t inited)
	{
		SetFieldIntValue(E_TB_ROLEBASE_FLD_INITED, inited)
	}
// --------- custom code_2 begin --------
// --------- custom code_2 end --------
};

#endif // __TB_ROLE_BASE_H__