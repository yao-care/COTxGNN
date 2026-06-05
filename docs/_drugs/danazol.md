---
layout: default
title: Danazol
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Danazol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Danazol: De Endometriosis a Amenorrea

## Resumen en Una Frase

Danazol es un esteroide sintético derivado de la 17α-etiniltestosterona, aprobado internacionalmente (FDA) para el tratamiento de endometriosis, enfermedad fibroquística de mama y angioedema hereditario, aunque no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea (inducción terapéutica)**, con **0 ensayos clínicos registrados** pero **20 publicaciones** que respaldan esta dirección, incluyendo 1 ECA y 1 revisión sistemática.
El mecanismo de acción de Danazol —supresión del eje hipotálamo-hipófisis-ovario— es precisamente el fundamento farmacológico de su capacidad para inducir amenorrea funcional.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Endometriosis / Enfermedad fibroquística de mama / Angioedema hereditario (aprobación FDA; sin registro INVIMA en Colombia) |
| Nueva Indicación Predicha | Amenorrea (inducción terapéutica) |
| Puntaje de Predicción TxGNN | 99.9995% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Danazol es un andrógeno atenuado derivado de la 17α-etiniltestosterona. Aunque los datos formales de MOA no están disponibles en la base de datos local consultada, la literatura científica es consistente: Danazol actúa a múltiples niveles del eje reproductivo. A nivel central, inhibe la secreción pulsátil de GnRH, lo que suprime la liberación de LH y FSH. A nivel gonadal, inhibe directamente las enzimas responsables de la esteroidogénesis ovárica, reduciendo la síntesis de estrógenos y progesterona. Adicionalmente, se une a proteínas transportadoras de esteroides en la circulación (SHBG, CBG), desplazando andrógenos endógenos y alterando el balance hormonal sistémico.

La relación entre la indicación original (endometriosis) y la nueva indicación predicha (amenorrea) es directa y mecanísticamente coherente: la amenorrea funcional es precisamente el estado hormonal que Danazol induce como efecto terapéutico en el tratamiento de la endometriosis. Al suprimir el ciclo menstrual, las lesiones endometriósicas se vuelven inactivas y regresan. La inducción de amenorrea terapéutica, por tanto, no es un efecto secundario a evitar, sino el mecanismo de acción central que se busca en poblaciones específicas (endometriosis activa, supresión menstrual en personas transgénero o en contextos militares).

El estudio de cohorte retrospectivo multicéntrico publicado en 2024 (PMID 39051650) documenta explícitamente el uso de Danazol para supresión menstrual en individuos transgénero, con tasas de amenorrea del 60–70% a los 6 meses. El ensayo clínico aleatorizado de 1990 (PMID 2140996) también reporta amenorrea como resultado primario verificado en el grupo Danazol durante el tratamiento de endometriosis. La predicción del modelo TxGNN refleja una relación farmacológica establecida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la combinación Danazol + Amenorrea.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | ECA | Fertility and Sterility | ECA doble ciego (n=82): Danazol 600 mg/día vs nafarelina en endometriosis; ambos tratamientos indujeron amenorrea funcional con regresión significativa de enfermedad activa |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Revisión Sistemática | Archives of Gynecology and Obstetrics | Metaanálisis sobre gestrinona en endometriosis; referencia a Danazol como inductor de amenorrea y atrofia endometrial como estándar comparador |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Cohorte Retrospectiva | Women's Health (London) | Cohorte multicéntrica en individuos transgénero: Danazol induce amenorrea y efectos androgénicos reversibles; eficacia del 60–70% a 6 meses |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | Journal of the Royal Army Medical Corps | Revisión sobre métodos de inducción terapéutica de amenorrea; Danazol discutido como opción viable versus anticonceptivos orales continuos y análogos GnRH |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Revisión | Journal of Reproductive Medicine | Revisión completa del mecanismo de Danazol: inhibición de gonadotropinas, supresión de esteroidogénesis gonadal y suprarrenal, efectos inmunoreguladores |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Revisión | Progress in Clinical and Biological Research | Revisión seminal sobre Danazol en endometriosis e infertilidad; describe la supresión ovárica y amenorrea como mecanismo central |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Revisión | Human Reproduction Update | Revisión de manejo de endometriosis; confirma que la regresión de lesiones ocurre durante estados de amenorrea o menopausia inducidos por Danazol u otros agentes |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause (New York) | Enfoque basado en evidencia para sangrado uterino anormal; Danazol mencionado como agente que puede inducir amenorrea con eficacia comprobada |
| [2013670](https://pubmed.ncbi.nlm.nih.gov/2013670/) | 1991 | Cohorte | Journal of Allergy and Clinical Immunology | Seguimiento a 13 años de Danazol en angioedema hereditario (n=56); dosis mínima efectiva de 200 mg/día; amenorrea irregular reportada como efecto secundario frecuente |
| [1807260](https://pubmed.ncbi.nlm.nih.gov/1807260/) | 1991 | Cohorte | Asian Pacific Journal of Allergy and Immunology | Danazol en trombocitopenia lúpica (n=7); reporta supresión menstrual como efecto colateral observado durante tratamiento |

---

## Información de Mercado en Colombia

Danazol no cuenta con registros sanitarios INVIMA activos en Colombia. El medicamento no se encuentra comercializado en el mercado colombiano a la fecha de corte del informe (junio 2026).

Para referencia comparativa, Danazol cuenta con aprobación vigente de la FDA (EE. UU.) para tres indicaciones:
1. Endometriosis
2. Enfermedad fibroquística de mama (mastalgia cíclica severa)
3. Angioedema hereditario (profilaxis)

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota clínica de la literatura:** PMID 18691993 documenta un caso de rabdomiólisis y pancreatitis por interacción Danazol 600 mg + lovastatina 40 mg (riesgo de miopatía aditiva). PMID 36744397 y PMID 34976488 advierten explícitamente que Danazol está **contraindicado durante el embarazo y la lactancia** por riesgo de virilización fetal/neonatal. Estos datos emergen de la literatura; la verificación formal del prospecto es indispensable antes de cualquier uso clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La inducción de amenorrea es el mecanismo de acción central de Danazol —no una indicación nueva, sino una extensión directa y bien documentada de su farmacología. Existe respaldo en 1 ECA, 1 revisión sistemática y múltiples cohortes; sin embargo, la ausencia de ensayos clínicos registrados específicamente para "amenorrea terapéutica" como indicación primaria, y la falta de registro en Colombia, impiden una recomendación Go sin condiciones.

**Para avanzar se necesita:**
- Obtener ficha técnica completa (prospecto INVIMA o FDA) para caracterizar contraindicaciones, advertencias de recuadro negro y perfil de interacciones farmacológicas formales
- Confirmar datos de MOA actualizados desde DrugBank API (DG002 pendiente)
- Definir la población objetivo específica para Colombia (endometriosis con supresión menstrual como fin, personas transgénero, u otra indicación)
- Evaluar viabilidad regulatoria de importación o registro ante INVIMA, dado que el medicamento no está comercializado actualmente en el país
- Considerar alternativas disponibles en Colombia (análogos GnRH, progestágenos de alta dosis) como comparadores activos en cualquier diseño de estudio futuro
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

