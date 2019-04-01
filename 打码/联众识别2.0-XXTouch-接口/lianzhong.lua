--[[
		lianzhong.lua
		
		Created by 桃子 on 18-06-26.
		Copyright (c) 2018年 桃子. All rights reserved.
		
		使用说明：
		1、请放置 lianzhong.lua 至设备 /var/mobile/Media/1ferver/lua/ 目录下
		2、写法
		
			local lz = require("lianzhong")		-- 加载模块
			local user = 'xxxxxxx'
			local pass = 'yyyyyyy'
			local img = screen.image(53,184,115,213)
			local typeid = '1001'
			
			-- 上传图⽚信息同时获取结果
			local Result, taskid_errmsg = lz.ocr(user, pass, img, typeid)
			if Result then
				sys.alert("识别成功\n结果："..Result.."\n题号："..taskid_errmsg)
			else
				sys.alert("失败\n原因："..taskid_errmsg)
			end
			
			-- 结果报错
			local Result, errmsg = lz.report_error(user, pass, taskid_errmsg)
			if Result then
				sys.alert("报错成功)
			else
				sys.alert("报错失败\n原因："..errmsg)
			end
			
			-- 检查点数
			local Result = lz.get_point(user, pass)
			if Result then
				sys.alert(table.concat({
					'查询成功',
					'剩余总点数：' .. Result.userPoints,
					'可用点数：' .. Result.availablePoints,
					'锁定点数：' .. Result.lockPoints
				}, '\r\n'))
			else
				sys.alert("查询失败")
			end
--]]
local softwareId = 10231
local softwareSecret = '5PJUuUI870vlsq7ajHt3bJLY4KeO71NUueZJI57n'


return {
	ocr = function(user, pass, img, typeid)
		-- 自适应图片对象 或 文件路径
		local img_base64_data
		if image.is(img) then
			img_base64_data = img:png_data():base64_encode()
		elseif file.exists(img) then
			img_base64_data = file.reads(img):base64_encode()
		else
			error('传入第三项值非图像对象或图像路径', 2)
		end
		
		local code, header, content = http.post(
			'https://v2-api.jsdama.com/upload',
			Timeout or 10,
			{
				['Host'] = 'v2-api.jsdama.com',
				['Connection'] = 'keep-alive',
				['Accept'] = 'application/json, text/javascript, */*; q=0.01',
				['User-Agent'] = 'XXTouch',
				['Content-Type'] = 'text/json',
			},
			json.encode({
				softwareId = softwareId,
				softwareSecret = softwareSecret,
				username = user,
				password = pass,
				captchaData = img_base64_data,
				captchaType = typeid,
				captchaMinLength = 0,
				captchaMaxLength = 0,
				workerTipsId = 0
			})
		)
		if code == 200 then
			local jobj = json.decode(content)
			if not jobj then return false, "无法解析的内容" end
			if jobj.code == 0 then
				return jobj.data.recognition, jobj.data.captchaId
			else
				return false, jobj.message
			end
		else
			return nil, '错误：超时'
		end
	end,
	report_error = function(user, pass, resultid)
		local code, header, content = http.post(
			'https://v2-api.jsdama.com/report-error',
			Timeout or 10,
			{
				['Host'] = 'v2-api.jsdama.com',
				['Connection'] = 'keep-alive',
				['Accept'] = 'application/json, text/javascript, */*; q=0.01',
				['User-Agent'] = 'XXTouch',
				['Content-Type'] = 'text/json',
			},
			json.encode({
				softwareId = softwareId,
				softwareSecret = softwareSecret,
				username = user,
				password = pass,
				captchaId = resultid
			})
		)
		if code == 200 then
			local jobj = json.decode(content)
			if not jobj then return false, "无法解析的内容" end
			if jobj.code == 0 then
				return jobj.data.result
			else
				return false, jobj.message
			end
		else
			return nil, '错误：超时'
		end
	end,
	get_point = function(user, pass)
		local code, header, content = http.post(
			'https://v2-api.jsdama.com/check-points',
			Timeout or 10,
			{
				['Host'] = 'v2-api.jsdama.com',
				['Connection'] = 'keep-alive',
				['Accept'] = 'application/json, text/javascript, */*; q=0.01',
				['User-Agent'] = 'XXTouch',
				['Content-Type'] = 'text/json',
			},
			json.encode({
				softwareId = softwareId,
				softwareSecret = softwareSecret,
				username = user,
				password = pass,
				captchaId = ID
			})
		)
		if code == 200 then
			local jobj = json.decode(content)
			if not jobj then return false, "无法解析的内容" end
			if jobj.code == 0 then
				return jobj.data
			else
				return false, jobj.message
			end
		else
			return nil, '错误：超时'
		end
	end
}



